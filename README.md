# a2n.Learn

Repo belajar Machine Learning lalu model AI, langkah demi langkah, untuk developer (.NET) yang ingin bisa membangun model sesuai kebutuhan.

## Peta fase
- **Fase 1 – Machine Learning** (`phase1-ml/`): 8 modul. Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.
- **Fase 2 – Model AI**: garis besar saja, lihat [docs/ROADMAP.md](docs/ROADMAP.md).

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 1 | [Persiapan](phase1-ml/modul-01-persiapan/) | Python, venv, Jupyter, Git, numpy/pandas | beginner | #1 |
| 2 | [Cara berpikir ML](phase1-ml/modul-02-cara-berpikir-ml/) | framing, train/test split, baseline, ukuran kesalahan | beginner | #2 |
| 3 | [Regresi](phase1-ml/modul-03-regresi/) | linear dan regularisasi | beginner | #3 |
| 4 | [Klasifikasi](phase1-ml/modul-04-klasifikasi/) | logistic regression, decision tree, random forest, gradient boosting | intermediate | #4 |
| 5 | [Evaluasi](phase1-ml/modul-05-evaluasi/) | cross-validation, confusion matrix, precision/recall, data leakage, pendalaman overfitting | intermediate | #5 |
| 6 | [Rekayasa fitur dan Pipeline](phase1-ml/modul-06-rekayasa-fitur/) | feature engineering dan scikit-learn Pipeline | advanced | #6 |
| 7 | [Tanpa label](phase1-ml/modul-07-tanpa-label/) | clustering, PCA, deteksi anomali | advanced | #7 |
| 8 | [Proyek akhir](phase1-ml/modul-08-proyek-akhir/) | data sintetis ala tambang, ekspor ONNX, panggil dari .NET | pro | #8 |

## Susunan modul
Setiap modul punya format sama: teori 1 halaman, notebook, kasus nyata, latihan + kunci, cek pemahaman. Detail di [docs/module-template.md](docs/module-template.md). Istilah dan perumpamaan dicatat di [docs/kamus-istilah.md](docs/kamus-istilah.md).

## Cara menjalankan (per modul)
```bash
cd phase1-ml/modul-01-persiapan
python3.14 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab            # buka notebook.ipynb, lalu Restart & Run All
pytest --nbmake *.ipynb
```
Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only. Dependensi per modul: `pyproject.toml` + `uv.lock`; `requirements.txt` hasil `uv export` di-commit.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan. Tanpa secret. Lihat [data/README.md](data/README.md).

## Kontribusi
Lihat [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
