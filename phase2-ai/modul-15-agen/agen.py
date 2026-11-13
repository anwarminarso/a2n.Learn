"""Agen dengan satu alat baca di dalam folder sandbox.

Tidak ada alat tulis, shell, atau jaringan.
"""

from pathlib import Path

ALAT = {
    "baca_berkas": {"aksi": "baca"},
}
ALLOW_LATIHAN = ("catatan.txt", "jadwal.txt")
FOLDER_SANDBOX = "sandbox"
KATA_DITOLAK = (
    "shell",
    "subprocess",
    "jaringan",
    "http://",
    "https://",
    "tulis berkas",
    "hapus berkas",
)


def daftar_alat():
    return tuple(ALAT)


def _di_dalam(tujuan, dasar):
    try:
        tujuan.relative_to(dasar)
    except ValueError:
        return False
    return True


def _alasan(sandbox, nama, allow):
    if not isinstance(nama, str) or nama.strip() == "":
        return "nama kosong", None
    huruf_drive = len(nama) >= 2 and nama[1] == ":"
    if huruf_drive or Path(nama).is_absolute():
        return "path absolut", None
    bagian = nama.replace("\\", "/").split("/")
    if any(potong == ".." for potong in bagian):
        return "path traversal", None
    if nama not in allow:
        return "di luar allowlist", None
    calon = Path(sandbox) / nama
    if not calon.exists() and not calon.is_symlink():
        return "tidak ada", None
    dasar = Path(sandbox).resolve()
    tujuan = calon.resolve()
    if not _di_dalam(tujuan, dasar):
        return "symlink", None
    if not tujuan.is_file():
        return "bukan berkas", None
    return "", tujuan


def baca_berkas(sandbox, nama, allow):
    alasan, tujuan = _alasan(sandbox, nama, allow)
    if alasan:
        return {"status": "tolak", "alasan": alasan, "teks": ""}
    teks = tujuan.read_text(encoding="utf-8")
    return {"status": "baca", "alasan": "", "teks": teks}


def langkah(perintah, sandbox, allow):
    if not isinstance(perintah, str) or perintah.strip() == "":
        return {"status": "tolak", "alasan": "perintah kosong", "teks": ""}
    rendah = perintah.lower()
    if any(kata in rendah for kata in KATA_DITOLAK):
        return {"status": "tolak", "alasan": "di luar alat", "teks": ""}
    if rendah.startswith("baca "):
        nama = perintah.split(maxsplit=1)[1].strip()
        return baca_berkas(sandbox, nama, allow)
    return {"status": "tolak", "alasan": "perintah tidak dikenal", "teks": ""}


def loop(perintah_list, sandbox, allow, batas=3):
    hasil = []
    for perintah in list(perintah_list)[:batas]:
        hasil.append(langkah(perintah, sandbox, allow))
        if hasil[-1]["status"] == "tolak":
            break
    return hasil
