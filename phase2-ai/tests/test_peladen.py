"""Tes peladen POST /jawab.

Offline. jawab() diganti stub. Port 0. Tidak mengunduh model.
"""

import ast
import http.client
import importlib.util
import inspect
import json
import socket
import threading
import time
from contextlib import contextmanager
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PELADEN = REPO / "phase2-ai" / "modul-15-agen" / "peladen.py"
JAWABAN = {
    "status": "bersumber",
    "sumber": "perpustakaan.txt",
    "skor": 0.9,
    "bagi": 4,
    "teks": "Kode rak buku cerita adalah B-12.",
}


def _muat():
    spec = importlib.util.spec_from_file_location("peladen15tes", PELADEN)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


@contextmanager
def _hidup(modul):
    server = modul.jalankan(0)
    utas = threading.Thread(target=server.serve_forever, daemon=True)
    utas.start()
    try:
        yield server
    finally:
        server.shutdown()
        utas.join(timeout=5)
        server.server_close()
        if utas.is_alive():
            raise RuntimeError("peladen tidak mati")


def _stub(monkeypatch, modul, panggilan):
    def palsu(pertanyaan, muatan, ambang_skor=0.3, ambang_bagi=2):
        panggilan.append((pertanyaan, muatan))
        return dict(JAWABAN)

    monkeypatch.setattr(modul, "jawab", palsu)


def _kirim(port, metode, jalur, badan=None, header_lebih=None):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
    try:
        if header_lebih is None:
            header = {}
            if badan is not None:
                header["Content-Type"] = "application/json"
            conn.request(metode, jalur, body=badan, headers=header)
        else:
            conn.putrequest(metode, jalur)
            for kunci, nilai in header_lebih:
                conn.putheader(kunci, nilai)
            conn.endheaders()
            if badan:
                conn.send(badan)
        respons = conn.getresponse()
        isi = respons.read()
        return respons.status, isi
    finally:
        conn.close()


def test_impor_tidak_menyalakan(monkeypatch):
    import http.server

    def tolak(*args, **kwargs):
        raise AssertionError("peladen menyala saat impor")

    monkeypatch.setattr(http.server, "HTTPServer", tolak)
    monkeypatch.setattr(http.server, "ThreadingHTTPServer", tolak)
    modul = _muat()
    assert modul.HOST == "127.0.0.1"
    assert list(inspect.signature(modul.jalankan).parameters) == ["port"]


def test_host_literal_tanpa_override():
    sumber = PELADEN.read_text(encoding="utf-8")
    pohon = ast.parse(sumber)
    host = []
    for node in ast.walk(pohon):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "HOST":
                    assert isinstance(node.value, ast.Constant)
                    assert node.value.value == "127.0.0.1"
                    host.append(node.value.value)
        if isinstance(node, ast.FunctionDef):
            nama = [a.arg for a in node.args.args]
            nama += [a.arg for a in node.args.kwonlyargs]
            assert "host" not in nama
            assert "alamat" not in nama
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert alias.name not in {"os", "argparse", "subprocess", "socket"}
        if isinstance(node, ast.ImportFrom):
            assert node.module not in {"os", "argparse", "subprocess", "socket"}
    assert host == ["127.0.0.1"]
    assert "argv" not in sumber
    assert "getenv" not in sumber
    assert "environ" not in sumber
    panggilan_main = []
    for node in pohon.body:
        if not isinstance(node, ast.If):
            continue
        for anak in ast.walk(node):
            if isinstance(anak, ast.Call) and getattr(anak.func, "id", "") == "jalankan":
                panggilan_main.append(anak)
    assert len(panggilan_main) == 1
    assert panggilan_main[0].args == []
    assert panggilan_main[0].keywords == []


def test_alamat_tetap_127(monkeypatch):
    monkeypatch.setenv("HOST", "10.1.2.3")
    monkeypatch.setenv("A2N_HOST", "10.9.8.7")
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        assert server.server_address[0] == "127.0.0.1"
        assert isinstance(server.server_address[1], int)
        assert server.server_address[1] > 0


def test_post_jawab_mengembalikan_json(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        badan = json.dumps({"pertanyaan": "kode rak buku cerita"}).encode("utf-8")
        status, isi = _kirim(port, "POST", "/jawab", badan)
    assert status == 200
    hasil = json.loads(isi.decode("utf-8"))
    assert hasil["status"] == "bersumber"
    assert hasil["sumber"] == "perpustakaan.txt"
    assert hasil["skor"] == 0.9
    assert panggilan[0][0] == "kode rak buku cerita"
    assert isinstance(panggilan[0][1], dict)


def test_jalur_lain_404(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        status_lain, _isi = _kirim(port, "GET", "/lain")
        status_post, _isi_post = _kirim(port, "POST", "/catatan", b"{}")
        status_metode, _isi_metode = _kirim(port, "GET", "/jawab")
    assert status_lain == 404
    assert status_post == 404
    assert status_metode == 405
    assert panggilan == []


def test_badan_terlalu_besar_tidak_memanggil_jawab(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        status, _isi = _kirim(
            port,
            "POST",
            "/jawab",
            header_lebih=(
                ("Content-Type", "application/json"),
                ("Content-Length", "4097"),
            ),
        )
    assert status == 413
    assert panggilan == []


def test_json_rusak_400(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        status, _isi = _kirim(port, "POST", "/jawab", b"{bukan json")
        status_kosong, _isi_kosong = _kirim(
            port,
            "POST",
            "/jawab",
            header_lebih=(("Content-Type", "application/json"),),
        )
    assert status == 400
    assert status_kosong == 411
    assert panggilan == []


def test_post_jawab_fungsi_asli():
    modul = _muat()
    with _hidup(modul) as server:
        port = server.server_address[1]
        badan = json.dumps({"pertanyaan": "kode rak buku cerita"}).encode("utf-8")
        status, isi = _kirim(port, "POST", "/jawab", badan)
    hasil = json.loads(isi.decode("utf-8"))
    assert status == 200
    assert hasil["status"] == "bersumber"
    assert hasil["sumber"] == "perpustakaan.txt"
    assert hasil["skor"] >= 0.3


def test_peladen_mati_bersih(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    server = modul.jalankan(0)
    port = server.server_address[1]
    utas = threading.Thread(target=server.serve_forever, daemon=True)
    utas.start()
    server.shutdown()
    utas.join(timeout=5)
    server.server_close()
    assert not utas.is_alive()
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=1)
    try:
        conn.request("GET", "/jawab")
        raise AssertionError("port masih menjawab")
    except OSError:
        pass
    finally:
        conn.close()


def test_badan_terpotong_tidak_menahan_berikutnya(monkeypatch):
    modul = _muat()
    assert modul.Penangan.timeout == 5
    monkeypatch.setattr(modul.Penangan, "timeout", 0.5)
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        soket = socket.create_connection(("127.0.0.1", port), timeout=3)
        try:
            soket.sendall(
                b"POST /jawab HTTP/1.1\r\n"
                b"Host: 127.0.0.1\r\n"
                b"Content-Type: application/json\r\n"
                b"Content-Length: 100\r\n"
                b"\r\n"
                b"{}"
            )
            mulai = time.monotonic()
            badan = json.dumps({"pertanyaan": "kode rak buku cerita"}).encode("utf-8")
            status, isi = _kirim(port, "POST", "/jawab", badan)
            assert time.monotonic() - mulai < 3
        finally:
            soket.close()
    hasil = json.loads(isi.decode("utf-8"))
    assert status == 200
    assert hasil["status"] == "bersumber"
    assert hasil["sumber"] == "perpustakaan.txt"
    assert hasil["skor"] == 0.9
    assert [tanya for tanya, _muatan in panggilan] == ["kode rak buku cerita"]


def test_chunked_tanpa_panjang_411(monkeypatch):
    modul = _muat()
    panggilan = []
    _stub(monkeypatch, modul, panggilan)
    with _hidup(modul) as server:
        port = server.server_address[1]
        isi_json = b'{"pertanyaan":"kode rak"}'
        permintaan = (
            b"POST /jawab HTTP/1.1\r\n"
            b"Host: 127.0.0.1\r\n"
            b"Content-Type: application/json\r\n"
            b"Transfer-Encoding: chunked\r\n"
            b"\r\n"
            + f"{len(isi_json):x}\r\n".encode("ascii")
            + isi_json
            + b"\r\n0\r\n\r\n"
        )
        with socket.create_connection(("127.0.0.1", port), timeout=3) as soket:
            soket.sendall(permintaan)
            data = b""
            while b"\r\n" not in data:
                bagian = soket.recv(4096)
                if not bagian:
                    break
                data += bagian
    status = data.split(b"\r\n", 1)[0].decode("ascii")
    assert status.split(" ")[1] == "411"
    assert panggilan == []
