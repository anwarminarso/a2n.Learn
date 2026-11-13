"""Potong teks, simpan vektor, lalu ambil potongan yang paling dekat.

Mode cepat memakai numpy dan SEED. Tidak mengunduh model.
Folder keluaran adalah indeks lokal. Folder itu tidak masuk repo.
"""

import json
from pathlib import Path

import numpy as np

UKURAN = 8
AWALAN_CATATAN = "Catatan:"
NAMA_BERKAS = "potongan.json"
FOLDER_INDEKS = "indeks"
AMBANG_SKOR = 0.3
AMBANG_BAGI = 2


def tokenkan(teks):
    return teks.lower().split()


def baca_dokumen(folder):
    folder = Path(folder)
    berkas = sorted(path for path in folder.glob("*.txt") if path.is_file())
    if not berkas:
        raise FileNotFoundError(folder)
    return [(path.name, path.read_text(encoding="utf-8")) for path in berkas]


def buat_potongan(dokumen):
    hasil = []
    for nama, teks in dokumen:
        for baris in teks.splitlines():
            bersih = baris.strip()
            if not bersih or bersih.startswith(AWALAN_CATATAN):
                continue
            hasil.append({"sumber": nama, "teks": bersih})
    return hasil


def _vektor_baru(teks, rng, peta):
    baris = []
    for tok in tokenkan(teks):
        if tok not in peta:
            peta[tok] = rng.normal(size=UKURAN)
        baris.append(peta[tok])
    return np.mean(np.vstack(baris), axis=0)


def bangun_indeks(potongan, seed, folder_keluar):
    rng = np.random.default_rng(seed)
    peta = {}
    baris = []
    for item in potongan:
        vektor = _vektor_baru(item["teks"], rng, peta)
        baris.append(
            {
                "sumber": item["sumber"],
                "teks": item["teks"],
                "vektor": [round(float(angka), 6) for angka in vektor],
            }
        )
    muatan = {
        "peta": {
            kata: [round(float(angka), 6) for angka in vektor]
            for kata, vektor in peta.items()
        },
        "potongan": baris,
    }
    folder = Path(folder_keluar)
    folder.mkdir(parents=True, exist_ok=True)
    tujuan = folder / NAMA_BERKAS
    teks = json.dumps(muatan, ensure_ascii=False, indent=2) + "\n"
    tujuan.write_text(teks, encoding="utf-8")
    return muatan


def muat_indeks(folder_keluar):
    path = Path(folder_keluar) / NAMA_BERKAS
    return json.loads(path.read_text(encoding="utf-8"))


def _vektor_kueri(teks, peta):
    baris = []
    for tok in tokenkan(teks):
        if tok in peta:
            baris.append(np.array(peta[tok], dtype=float))
    if not baris:
        return np.zeros(UKURAN)
    return np.mean(np.vstack(baris), axis=0)


def _kemiripan(kiri, kanan):
    norma_kiri = float(np.linalg.norm(kiri))
    norma_kanan = float(np.linalg.norm(kanan))
    if norma_kiri == 0.0 or norma_kanan == 0.0:
        return 0.0
    return float(kiri @ kanan / (norma_kiri * norma_kanan))


def peringkat(pertanyaan, muatan):
    vektor = _vektor_kueri(pertanyaan, muatan["peta"])
    kata_tanya = set(tokenkan(pertanyaan))
    hasil = []
    for item in muatan["potongan"]:
        skor = _kemiripan(vektor, np.array(item["vektor"], dtype=float))
        bagi = len(kata_tanya & set(tokenkan(item["teks"])))
        hasil.append(
            {
                "skor": skor,
                "bagi": bagi,
                "sumber": item["sumber"],
                "teks": item["teks"],
            }
        )
    hasil.sort(key=lambda row: (-row["skor"], -row["bagi"], row["sumber"], row["teks"]))
    return hasil


def jawab(pertanyaan, muatan, ambang_skor=AMBANG_SKOR, ambang_bagi=AMBANG_BAGI):
    terbaik = peringkat(pertanyaan, muatan)[0]
    if terbaik["bagi"] < ambang_bagi or terbaik["skor"] < ambang_skor:
        return {
            "status": "jawaban_mengarang",
            "skor": terbaik["skor"],
            "bagi": terbaik["bagi"],
            "sumber": "",
            "teks": "",
        }
    return {
        "status": "bersumber",
        "skor": terbaik["skor"],
        "bagi": terbaik["bagi"],
        "sumber": terbaik["sumber"],
        "teks": terbaik["teks"],
    }
