# a2n.Learn

Repo belajar Machine Learning lalu model AI, langkah demi langkah, untuk developer (.NET) yang ingin bisa membangun model sesuai kebutuhan.

## Peta fase
- **Fase 1 – Machine Learning** (`phase1-ml/`): 8 modul, ± 1 minggu per modul.
- **Fase 2 – Model AI**: garis besar saja, lihat [docs/ROADMAP.md](docs/ROADMAP.md).

| # | Modul | Topik | Issue |
|---|---|---|---|
| 1 | [Persiapan](phase1-ml/modul-01-persiapan/) | Python, venv, Jupyter, Git, numpy/pandas | #1 |
| 2 | [Cara berpikir ML](phase1-ml/modul-02-cara-berpikir-ml/) | framing, train/test split, data leakage, metrik | #2 |
| 3 | [Regresi](phase1-ml/modul-03-regresi/) | linear dan regularisasi | #3 |
| 4 | [Klasifikasi](phase1-ml/modul-04-klasifikasi/) | logistic regression, decision tree, random forest, gradient boosting | #4 |
| 5 | [Evaluasi](phase1-ml/modul-05-evaluasi/) | cross-validation, confusion matrix, precision/recall, overfitting | #5 |
| 6 | [Rekayasa fitur dan Pipeline](phase1-ml/modul-06-rekayasa-fitur/) | feature engineering dan scikit-learn Pipeline | #6 |
| 7 | [Tanpa label](phase1-ml/modul-07-tanpa-label/) | clustering, PCA, deteksi anomali | #7 |
| 8 | [Proyek akhir](phase1-ml/modul-08-proyek-akhir/) | data publik, ekspor ONNX, panggil dari .NET | #8 |

## Susunan modul
Setiap modul punya format sama: teori 1 halaman, notebook, kasus nyata, latihan + kunci, cek pemahaman. Detail di [docs/module-template.md](docs/module-template.md).

## Cara menjalankan (per modul)
```bash
cd phase1-ml/modul-01-persiapan
python3.12 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab            # buka notebook.ipynb, lalu Restart & Run All
pytest --nbmake *.ipynb
```
Python 3.12, CPU only. `requirements.txt` di-pin dari `uv.lock` (`uv export`).

## Aturan data
Hanya dataset bawaan scikit-learn atau data sintetis yang dibangkitkan kode. **Dilarang** memakai data ANTAM/internal atau menyimpan secret. Lihat [data/README.md](data/README.md).

## Kontribusi
Lihat [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
