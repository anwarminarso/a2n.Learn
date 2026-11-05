# a2n.Learn

Repo belajar Machine Learning lalu model AI, langkah demi langkah, untuk developer (.NET) yang ingin bisa membangun model sesuai kebutuhan.

## Peta fase
- **Fase 1 – Machine Learning** (`phase1-ml/`): 8 modul yang dipecah menjadi 12 bagian. Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.
- **Fase 2 – Model AI**: garis besar saja, lihat [docs/ROADMAP.md](docs/ROADMAP.md).

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 1 | [Persiapan](phase1-ml/modul-01-persiapan/) | Python, venv, Jupyter, Git, numpy/pandas | beginner | #1 |
| 2 | [Cara berpikir ML](phase1-ml/modul-02-cara-berpikir-ml/) | framing, train/test split, baseline, ukuran kesalahan | beginner | #2 |
| 3 | [Regresi](phase1-ml/modul-03-regresi/) | regresi linear dan fungsi loss | beginner | #3 |
| 3b | Regularisasi (Ridge dan Lasso) | regularisasi: Ridge dan Lasso | intermediate | #18 |
| 4a | Klasifikasi | regresi logistik dan pohon keputusan | intermediate | #4 |
| 4b | Pohon dan model gabungan | hutan acak dan gradient boosting | intermediate | #4 |
| 5a | Validasi dan overfitting | data leakage, cross-validation, overfitting | intermediate | #5 |
| 5b | Metrik penilaian dan ujian Intermediate | confusion matrix, precision, recall | intermediate | #5 |
| 6a | Rekayasa fitur | fitur, encoding, penskalaan | advanced | #6 |
| 6b | Pipeline | Pipeline dan ColumnTransformer | advanced | #6 |
| 7 | [Tanpa label](phase1-ml/modul-07-tanpa-label/) | clustering, PCA, deteksi anomali | advanced | #7 |
| 8 | [Proyek akhir](phase1-ml/modul-08-proyek-akhir/) | data sintetis ala tambang, ekspor ONNX, panggil dari .NET | pro | #8 |

## Susunan modul
Setiap modul punya format sama: teori 1 halaman, notebook, kasus nyata, latihan + kunci, cek pemahaman. Detail di [docs/module-template.md](docs/module-template.md). Istilah dan perumpamaan dicatat di [docs/kamus-istilah.md](docs/kamus-istilah.md).

## Cara menjalankan
Perintah dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`):

```bash
uv sync --frozen
uv run pytest --nbmake
```

Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only. Dependensi ada di `pyproject.toml` dan `uv.lock` di root repo. `requirements.txt` adalah hasil `uv export` dari lock itu.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan. Tanpa secret. Lihat [data/README.md](data/README.md).

## Kontribusi
Lihat [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
