"""Tes korpus RAG dan sandbox agen.

Mode cepat. Tidak mengunduh model dan tidak memakai torch.
"""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
FASE2 = REPO / "phase2-ai"
JARUM_ALAT = (
    "import subprocess",
    "from subprocess",
    "os.system",
    "import socket",
    "urlopen",
    "import requests",
    "http.client",
    "Popen(",
    "write_text(",
    "mkdir(",
    "open(",
)


def _muat(path, nama):
    spec = importlib.util.spec_from_file_location(nama, path)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def _agen():
    return _muat(FASE2 / "modul-15-agen" / "agen.py", "agen15tes")


def _rag():
    return _muat(FASE2 / "modul-14-rag" / "rag.py", "rag14tes")


def test_korpus_sintetis_tercommit_dan_indeks_diabaikan():
    dokumen = FASE2 / "modul-14-rag" / "dokumen"
    berkas = sorted(dokumen.glob("*.txt"))
    assert len(berkas) >= 3
    terlacak = subprocess.check_output(
        ["git", "ls-files", "phase2-ai/modul-14-rag/dokumen"],
        cwd=REPO,
        text=True,
    ).splitlines()
    for path in berkas:
        rel = path.relative_to(REPO).as_posix()
        assert rel in terlacak
        teks = path.read_text(encoding="utf-8")
        assert "teks sintetis" in teks
        assert "data asli perusahaan" in teks
        abaikan = subprocess.run(["git", "check-ignore", "-q", rel], cwd=REPO)
        assert abaikan.returncode == 1
    rag = _rag()
    potongan = rag.buat_potongan(rag.baca_dokumen(dokumen))
    assert potongan
    nama = {path.name for path in berkas}
    for item in potongan:
        assert item["sumber"] in nama
        assert item["teks"] in (dokumen / item["sumber"]).read_text(encoding="utf-8")
    gitignore = (REPO / ".gitignore").read_text(encoding="utf-8")
    assert "phase2-ai/modul-14-rag/indeks/" in gitignore
    indeks = subprocess.run(
        ["git", "check-ignore", "-q", "phase2-ai/modul-14-rag/indeks/potongan.json"],
        cwd=REPO,
    )
    assert indeks.returncode == 0
    terlacak_indeks = subprocess.check_output(
        ["git", "ls-files", "phase2-ai/modul-14-rag/indeks"],
        cwd=REPO,
        text=True,
    )
    assert terlacak_indeks.strip() == ""


def test_pembangun_hanya_membaca_folder_dokumen(tmp_path):
    luar = tmp_path / "rahasia.txt"
    luar.write_text("rahasia-luar", encoding="utf-8")
    dalam = tmp_path / "dokumen"
    dalam.mkdir()
    (dalam / "satu.txt").write_text(
        "Catatan: teks sintetis untuk latihan. Bukan data asli perusahaan.\n"
        "Kalimat kebun kecil.\n",
        encoding="utf-8",
    )
    rag = _rag()
    dokumen = rag.baca_dokumen(dalam)
    assert [nama for nama, _teks in dokumen] == ["satu.txt"]
    assert "rahasia-luar" not in json.dumps(dokumen)
    muatan = rag.bangun_indeks(rag.buat_potongan(dokumen), 42, tmp_path / "indeks")
    assert "rahasia-luar" not in json.dumps(muatan)
    assert (tmp_path / "indeks" / "potongan.json").is_file()


def test_daftar_alat_hanya_baca():
    agen = _agen()
    assert agen.daftar_alat() == ("baca_berkas",)
    assert set(agen.ALAT) == {"baca_berkas"}
    assert agen.ALAT["baca_berkas"]["aksi"] == "baca"
    teks = (FASE2 / "modul-15-agen" / "agen.py").read_text(encoding="utf-8")
    for jarum in JARUM_ALAT:
        assert jarum not in teks


def test_baca_allowlist_berhasil(tmp_path):
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    (sandbox / "catatan.txt").write_text("halo arsip", encoding="utf-8")
    hasil = _agen().baca_berkas(sandbox, "catatan.txt", ("catatan.txt",))
    assert hasil["status"] == "baca"
    assert hasil["teks"] == "halo arsip"


def test_path_traversal_ditolak(tmp_path):
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    rahasia = tmp_path / "rahasia.txt"
    rahasia.write_text("rahasia-traversal", encoding="utf-8")
    (sandbox / "catatan.txt").write_text("boleh", encoding="utf-8")
    hasil = _agen().baca_berkas(sandbox, "../rahasia.txt", ("catatan.txt",))
    assert hasil["status"] == "tolak"
    assert hasil["alasan"] == "path traversal"
    assert hasil["teks"] == ""
    assert "rahasia-traversal" not in hasil["teks"]


def test_path_absolut_ditolak(tmp_path):
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    rahasia = tmp_path / "rahasia.txt"
    rahasia.write_text("rahasia-absolut", encoding="utf-8")
    hasil = _agen().baca_berkas(sandbox, str(rahasia), ("catatan.txt",))
    assert hasil["status"] == "tolak"
    assert hasil["alasan"] == "path absolut"
    assert hasil["teks"] == ""
    assert "rahasia-absolut" not in hasil["teks"]


def test_symlink_keluar_sandbox_ditolak(tmp_path):
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    rahasia = tmp_path / "rahasia.txt"
    rahasia.write_text("rahasia-symlink", encoding="utf-8")
    tautan = sandbox / "catatan.txt"
    tautan.symlink_to(rahasia)
    hasil = _agen().baca_berkas(sandbox, "catatan.txt", ("catatan.txt",))
    assert hasil["status"] == "tolak"
    assert hasil["alasan"] == "symlink"
    assert hasil["teks"] == ""
    assert "rahasia-symlink" not in hasil["teks"]


def test_berkas_di_luar_allowlist_ditolak(tmp_path):
    sandbox = tmp_path / "sandbox"
    sandbox.mkdir()
    (sandbox / "samping.txt").write_text("jangan dibaca", encoding="utf-8")
    hasil = _agen().baca_berkas(sandbox, "samping.txt", ("catatan.txt",))
    assert hasil["status"] == "tolak"
    assert hasil["alasan"] == "di luar allowlist"
    assert hasil["teks"] == ""


def test_unduh_modul_baru_butuh_bendera(monkeypatch):
    monkeypatch.delenv("A2N_UNDUH", raising=False)
    for folder, fungsi in (
        ("modul-14-rag", "muat_embedding"),
        ("modul-14-rag", "muat_jawaban"),
        ("modul-15-agen", "muat_agen"),
    ):
        modul = _muat(FASE2 / folder / "muat.py", "muat_" + fungsi)
        with pytest.raises(RuntimeError, match="A2N_UNDUH"):
            getattr(modul, fungsi)()
