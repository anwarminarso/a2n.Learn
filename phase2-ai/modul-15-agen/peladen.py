"""Peladen kecil untuk pertanyaan dari program .NET.

Hanya mengikat 127.0.0.1. Alamat itu tidak dibaca dari argumen
atau dari variabel lingkungan. Berkas ini tidak menyalakan peladen
saat diimpor. Yang dilayani hanya POST /jawab, lewat jawab() modul 14.
"""

import importlib.util
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from tempfile import TemporaryDirectory

HOST = "127.0.0.1"
BATAS_BADAN = 4 * 1024
JALUR = "/jawab"
SEED = 42

_FOLDER_RAG = Path(__file__).resolve().parents[1] / "modul-14-rag"
_RAG = _FOLDER_RAG / "rag.py"
_DOKUMEN = _FOLDER_RAG / "dokumen"


def _muat_rag():
    spec = importlib.util.spec_from_file_location("rag14_peladen", _RAG)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


_rag = _muat_rag()
jawab = _rag.jawab


def _muatan():
    dokumen = _rag.baca_dokumen(_DOKUMEN)
    potongan = _rag.buat_potongan(dokumen)
    with TemporaryDirectory() as folder:
        return _rag.bangun_indeks(potongan, SEED, folder)


def _ukuran_badan(header):
    daftar = header.get_all("Content-Length")
    if not daftar:
        return 411, None
    if len(daftar) != 1:
        return 400, None
    mentah = daftar[0].strip()
    if not mentah.isdigit():
        return 400, None
    ukuran = int(mentah)
    if ukuran > BATAS_BADAN:
        return 413, None
    return None, ukuran


class Penangan(BaseHTTPRequestHandler):
    def _jalur(self):
        return self.path.split("?", 1)[0]

    def _kirim(self, kode, muatan):
        tubuh = json.dumps(muatan, ensure_ascii=False).encode("utf-8")
        self.send_response(kode)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(tubuh)))
        if kode == 405:
            self.send_header("Allow", "POST")
        self.end_headers()
        self.wfile.write(tubuh)

    def _bukan_post(self):
        if self._jalur() != JALUR:
            self._kirim(404, {"status": "tidak_ada"})
            return
        self._kirim(405, {"status": "metode"})

    def do_GET(self):
        self._bukan_post()

    def do_PUT(self):
        self._bukan_post()

    def do_DELETE(self):
        self._bukan_post()

    def do_PATCH(self):
        self._bukan_post()

    def do_HEAD(self):
        self._bukan_post()

    def do_OPTIONS(self):
        self._bukan_post()

    def do_POST(self):
        if self._jalur() != JALUR:
            self._kirim(404, {"status": "tidak_ada"})
            return
        kode, ukuran = _ukuran_badan(self.headers)
        if kode is not None:
            self._kirim(kode, {"status": "badan"})
            return
        try:
            teks = self.rfile.read(ukuran).decode("utf-8")
            data = json.loads(teks)
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._kirim(400, {"status": "json"})
            return
        if not isinstance(data, dict):
            self._kirim(400, {"status": "json"})
            return
        pertanyaan = data.get("pertanyaan")
        if not isinstance(pertanyaan, str) or pertanyaan.strip() == "":
            self._kirim(400, {"status": "json"})
            return
        hasil = jawab(pertanyaan, self.server.muatan)
        self._kirim(200, hasil)

    def log_message(self, fmt, *args):
        return


def jalankan(port=8765):
    """Ikat 127.0.0.1 pada port ini. Port 0 memilih port kosong.

    Peladen yang kembali sudah terikat, tetapi belum melayani.
    Pemanggil menjalankan serve_forever, lalu shutdown dari utas lain.
    """
    muatan = _muatan()
    server = HTTPServer((HOST, port), Penangan)
    server.muatan = muatan
    return server


if __name__ == "__main__":
    peladen = jalankan()
    try:
        peladen.serve_forever()
    finally:
        peladen.server_close()
