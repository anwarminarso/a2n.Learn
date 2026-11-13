# a2n.Learn

Repo belajar Machine Learning lalu model AI, langkah demi langkah, untuk developer (.NET) yang ingin bisa membangun model sesuai kebutuhan.

## Peta fase
- **Fase 1 – Machine Learning** (`phase1-ml/`): 8 modul yang dipecah menjadi 12 bagian. Satu modul cukup untuk satu sesi duduk.
- **Fase 2 – Model AI** (`phase2-ai/`): 7 modul utuh. Modul 9 sampai 15 sudah berisi materi mode cepat. Issue [#26](https://github.com/anwarminarso/a2n.Learn/issues/26) sampai [#32](https://github.com/anwarminarso/a2n.Learn/issues/32), tracking [#33](https://github.com/anwarminarso/a2n.Learn/issues/33). Urutan ada di [docs/ROADMAP.md](docs/ROADMAP.md). Register model ada di [docs/lisensi-model.md](docs/lisensi-model.md).

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 1 | [Persiapan](phase1-ml/modul-01-persiapan/) | Python, venv, Jupyter, Git, numpy/pandas | beginner | [#1](https://github.com/anwarminarso/a2n.Learn/issues/1) |
| 2 | [Cara berpikir ML](phase1-ml/modul-02-cara-berpikir-ml/) | framing, train/test split, baseline, ukuran kesalahan | beginner | [#2](https://github.com/anwarminarso/a2n.Learn/issues/2) |
| 3 | [Regresi](phase1-ml/modul-03-regresi/) | regresi linear dan fungsi loss | beginner | [#3](https://github.com/anwarminarso/a2n.Learn/issues/3) |
| 3b | [Regularisasi (Ridge dan Lasso)](phase1-ml/modul-03b-regularisasi/) | regularisasi: Ridge dan Lasso | intermediate | [#18](https://github.com/anwarminarso/a2n.Learn/issues/18) |
| 4a | [Klasifikasi](phase1-ml/modul-04a-klasifikasi/) | regresi logistik dan pohon keputusan | intermediate | [#4](https://github.com/anwarminarso/a2n.Learn/issues/4) |
| 4b | [Pohon dan model gabungan](phase1-ml/modul-04b-pohon-gabungan/) | hutan acak dan gradient boosting | intermediate | [#4](https://github.com/anwarminarso/a2n.Learn/issues/4) |
| 5a | [Validasi dan overfitting](phase1-ml/modul-05a-validasi-overfitting/) | data leakage, cross-validation, overfitting | intermediate | [#5](https://github.com/anwarminarso/a2n.Learn/issues/5) |
| 5b | [Metrik penilaian dan ujian Intermediate](phase1-ml/modul-05b-metrik-penilaian/) | confusion matrix, precision, recall | intermediate | [#5](https://github.com/anwarminarso/a2n.Learn/issues/5) |
| 6a | [Rekayasa fitur](phase1-ml/modul-06a-rekayasa-fitur/) | fitur, encoding, penskalaan | advanced | [#6](https://github.com/anwarminarso/a2n.Learn/issues/6) |
| 6b | [Pipeline](phase1-ml/modul-06b-pipeline/) | Pipeline dan ColumnTransformer | advanced | [#6](https://github.com/anwarminarso/a2n.Learn/issues/6) |
| 7 | [Tanpa label](phase1-ml/modul-07-tanpa-label/) | clustering, PCA, deteksi anomali | advanced | [#7](https://github.com/anwarminarso/a2n.Learn/issues/7) |
| 8 | [Proyek akhir](phase1-ml/modul-08-proyek-akhir/) | data sintetis ala tambang, ekspor ONNX, panggil dari .NET | pro | [#8](https://github.com/anwarminarso/a2n.Learn/issues/8) |

### Fase 2

Modul 9 sampai 15 sudah berisi materi mode cepat. Tujuh modul utuh. Issue mengikuti tabel di `docs/ROADMAP.md`. Kolom tingkat pada tabel di bawah kosong.

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 9 | [Dasar jaringan saraf dan PyTorch](phase2-ai/modul-09-pytorch/) | tensor, autograd, dan jaringan saraf pertama | — | [#26](https://github.com/anwarminarso/a2n.Learn/issues/26) |
| 10 | [Embedding dan tokenisasi](phase2-ai/modul-10-tokenisasi-embedding/) | token, embedding, kemiripan vektor | — | [#27](https://github.com/anwarminarso/a2n.Learn/issues/27) |
| 11 | [Transformer](phase2-ai/modul-11-attention-transformer/) | attention dari nol, lalu model kecil untuk klasifikasi teks | — | [#28](https://github.com/anwarminarso/a2n.Learn/issues/28) |
| 12 | [Fine-tune dengan LoRA](phase2-ai/modul-12-lora/) | penyetelan halus (fine-tune), ukur sebelum dan sesudah | — | [#29](https://github.com/anwarminarso/a2n.Learn/issues/29) |
| 13 | [Menjalankan model lokal dengan Ollama](phase2-ai/modul-13-model-lokal/) | merge LoRA, GGUF, impor Ollama, kontrol jalur sama | — | [#30](https://github.com/anwarminarso/a2n.Learn/issues/30) |
| 14 | [RAG (Retrieval-Augmented Generation)](phase2-ai/modul-14-rag/) | potongan, penyimpan vektor, jawaban dengan sumber, penolakan tanpa_sumber | — | [#31](https://github.com/anwarminarso/a2n.Learn/issues/31) |
| 15 | [Agen dan proyek akhir Fase 2](phase2-ai/modul-15-agen/) | loop agen, proyek akhir RAG plus agen, panggilan .NET lewat HTTP | — | [#32](https://github.com/anwarminarso/a2n.Learn/issues/32) |

## Susunan modul
Setiap modul punya format sama: teori 1 halaman, notebook, kasus nyata, latihan + kunci, cek pemahaman. Detail di [docs/module-template.md](docs/module-template.md). Istilah dan perumpamaan dicatat di [docs/kamus-istilah.md](docs/kamus-istilah.md).

Modul 9 sampai 15 punya notebook, latihan, dan kunci. Grup torch opsional, CPU saja, tidak ikut `uv sync` biasa: `uv sync --frozen --group torch`.

## Cara menjalankan
Perintah dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`):

```bash
uv sync --frozen
uv run pytest --nbmake
```

Python 3.14, dipin proyek, CPU only. Dependensi ada di `pyproject.toml` dan `uv.lock` di root repo. `requirements.txt` adalah hasil `uv export` dari lock itu.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui pengelola materi dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan. Tanpa secret. Lihat [data/README.md](data/README.md).

Fase 2, di README tiap modul `phase2-ai/`: data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan. Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Unduhan model hanya model kecil berlisensi Apache-2.0 atau MIT, dan lisensi dicek sebelum unduh. Register ada di [docs/lisensi-model.md](docs/lisensi-model.md). Urutan modul ada di [docs/ROADMAP.md](docs/ROADMAP.md).

## Kontribusi
Lihat [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
