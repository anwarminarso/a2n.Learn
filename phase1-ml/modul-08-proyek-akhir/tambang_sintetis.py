"""Generator data sintetis bergaya catatan batch olahan mineral.

Bukan pengukuran lapangan. Bukan data asli perusahaan.
Tidak ada berkas yang diunduh.

Parameter dicocokkan ke dokumentasi NumPy, bukan ke make_regression:
- seed masuk ke numpy.random.default_rng dan hanya mengunci keadaan
  pembangkit. Bukan simpangan derau dan bukan geseran tetap.
- Generator.normal(loc, scale): loc adalah rata-rata gangguan Gauss,
  scale adalah simpangan bakunya.
- skala mengalikan gangguan itu, jadi simpangan baku tiap kolom sama
  dengan skala kolom tersebut. Rata-rata gangguan tetap 0.
- pusat adalah nilai tengah fitur untuk tiap kelas, ditambah sesudah
  gangguan. Bukan bias pada jawaban.
"""

import numpy as np
import pandas as pd

NAMA_FITUR = (
    "kadar_logam_persen",
    "kadar_air_persen",
    "ukuran_butir_mm",
    "kedalaman_m",
)
NAMA_KELAS = ("sisihkan", "campur", "simpan")
N_PER_KELAS = 80


def buat_batch(seed):
    """Bangun satu tabel batch.

    `seed` hanya argumen default_rng: mengunci keadaan pembangkit.
    """
    rng = np.random.default_rng(seed)
    kelas = np.repeat(np.arange(len(NAMA_KELAS)), N_PER_KELAS)
    pusat = np.array(
        [
            [1.4, 11.0, 8.0, 28.0],
            [4.2, 6.5, 4.0, 52.0],
            [7.8, 2.8, 1.6, 16.0],
        ],
        dtype=float,
    )
    skala = np.array([0.30, 0.70, 0.45, 2.5], dtype=float)
    # loc=0 rata-rata gangguan, scale=1 simpangan baku sebelum dikali skala.
    # pusat menggeser fitur tiap kelas, bukan jawaban.
    angka = pusat[kelas] + rng.normal(0.0, 1.0, size=(kelas.shape[0], 4)) * skala
    urutan = rng.permutation(kelas.shape[0])
    tabel = pd.DataFrame(angka[urutan], columns=NAMA_FITUR)
    tabel["kelas"] = kelas[urutan].astype(int)
    return tabel
