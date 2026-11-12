# a2n.Learn

Repo belajar Machine Learning lalu model AI, langkah demi langkah, untuk developer (.NET) yang ingin bisa membangun model sesuai kebutuhan.

## Peta fase
- **Fase 1 – Machine Learning** (`phase1-ml/`): 8 modul yang dipecah menjadi 12 bagian. Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas.
- **Fase 2 – Model AI** (`phase2-ai/`): 7 topik dipecah menjadi 10 modul, status PLACEHOLDER. Satu modul cukup untuk satu sesi duduk. Rencana ada di [docs/ROADMAP.md](docs/ROADMAP.md).

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 1 | [Persiapan](phase1-ml/modul-01-persiapan/) | Python, venv, Jupyter, Git, numpy/pandas | beginner | #1 |
| 2 | [Cara berpikir ML](phase1-ml/modul-02-cara-berpikir-ml/) | framing, train/test split, baseline, ukuran kesalahan | beginner | #2 |
| 3 | [Regresi](phase1-ml/modul-03-regresi/) | regresi linear dan fungsi loss | beginner | #3 |
| 3b | Regularisasi (Ridge dan Lasso) | regularisasi: Ridge dan Lasso | intermediate | #18 |
| 4a | [Klasifikasi](phase1-ml/modul-04a-klasifikasi/) | regresi logistik dan pohon keputusan | intermediate | #4 |
| 4b | [Pohon dan model gabungan](phase1-ml/modul-04b-pohon-gabungan/) | hutan acak dan gradient boosting | intermediate | #4 |
| 5a | [Validasi dan overfitting](phase1-ml/modul-05a-validasi-overfitting/) | data leakage, cross-validation, overfitting | intermediate | #5 |
| 5b | [Metrik penilaian dan ujian Intermediate](phase1-ml/modul-05b-metrik-penilaian/) | confusion matrix, precision, recall | intermediate | #5 |
| 6a | [Rekayasa fitur](phase1-ml/modul-06a-rekayasa-fitur/) | fitur, encoding, penskalaan | advanced | #6 |
| 6b | [Pipeline](phase1-ml/modul-06b-pipeline/) | Pipeline dan ColumnTransformer | advanced | #6 |
| 7 | [Tanpa label](phase1-ml/modul-07-tanpa-label/) | clustering, PCA, deteksi anomali | advanced | #7 |
| 8 | [Proyek akhir](phase1-ml/modul-08-proyek-akhir/) | data sintetis ala tambang, ekspor ONNX, panggil dari .NET | pro | #8 |

### Fase 2

Materi belum ditulis. Issue dibuat terpisah oleh PM, jadi kolom Issue berisi —.

| # | Modul | Topik | Tingkat | Issue |
|---|---|---|---|---|
| 9a | [Tensor dan autograd](phase2-ai/modul-09a-tensor-autograd/) | tensor, autograd, gradien | pro | — |
| 9b | [Jaringan saraf kecil dan putaran latihan](phase2-ai/modul-09b-jaringan-saraf/) | jaringan kecil, putaran latihan, bandingkan dengan Fase 1 | pro | — |
| 10 | [Embedding dan tokenisasi](phase2-ai/modul-10-embedding-tokenisasi/) | token, embedding, kemiripan vektor | pro | — |
| 11a | [Attention skala mini](phase2-ai/modul-11a-attention/) | attention dari nol pada matriks mini | pro | — |
| 11b | [Klasifikasi teks dengan model siap pakai](phase2-ai/modul-11b-klasifikasi-teks/) | klasifikasi teks dengan model Hugging Face | pro | — |
| 12 | [Penyelarasan dengan LoRA](phase2-ai/modul-12-lora/) | penyelarasan LoRA, ukur sebelum dan sesudah | pro | — |
| 13 | [Menjalankan model lokal](phase2-ai/modul-13-model-lokal/) | GGUF, Ollama, kontrol tanpa LoRA | pro | — |
| 14a | [Potongan teks dan penyimpan vektor](phase2-ai/modul-14a-penyimpan-vektor/) | potongan, penyimpan vektor, pengambilan | pro | — |
| 14b | [Jawaban dengan sumber](phase2-ai/modul-14b-jawaban-sumber/) | jawaban dengan sumber dan jawaban mengarang | pro | — |
| 15 | [Agen](phase2-ai/modul-15-agen/) | pemanggilan alat, loop agen, injeksi prompt | pro | — |

## Susunan modul
Setiap modul punya format sama: teori 1 halaman, notebook, kasus nyata, latihan + kunci, cek pemahaman. Detail di [docs/module-template.md](docs/module-template.md). Istilah dan perumpamaan dicatat di [docs/kamus-istilah.md](docs/kamus-istilah.md).

Modul Fase 2 yang berstatus PLACEHOLDER baru berisi README rencana. Notebook, latihan, dan kunci menyusul bersama materi.

## Cara menjalankan
Perintah dijalankan dari root repo (folder yang berisi `pyproject.toml` dan `uv.lock`):

```bash
uv sync --frozen
uv run pytest --nbmake
```

Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10), CPU only. Dependensi ada di `pyproject.toml` dan `uv.lock` di root repo. `requirements.txt` adalah hasil `uv export` dari lock itu.

## Aturan data
Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan. Tanpa secret. Lihat [data/README.md](data/README.md).

Fase 2 menambah aturan di README tiap modul `phase2-ai/` dan di [docs/ROADMAP.md](docs/ROADMAP.md): model serta dataset Hugging Face di-pin ke revisi, hanya format safetensors, `trust_remote_code=False`, dan lisensi tiap model dicatat. Dataset, adapter LoRA, dan indeks vektor dari data non-publik tidak boleh masuk repo atau di-push ke Hugging Face.

## Kontribusi
Lihat [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
