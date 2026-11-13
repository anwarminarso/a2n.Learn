# Roadmap

Versi Python: Python 3.14 (versi stabil terbaru yang masih bugfix; EOL 2030-10); detail dan aturan fallback di [CONTRIBUTING.md](CONTRIBUTING.md#versi-python).

Aturan data: Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data asli perusahaan.

Istilah yang dipakai di semua modul dicatat di [kamus-istilah.md](kamus-istilah.md).

## Fase 1 – Machine Learning
Urutan wajib: modul berikutnya baru dimulai setelah modul sebelumnya lolos Ursa (PASS) dan Squal (PASS / PASS BERSYARAT). Modul 1 dikerjakan pertama oleh Pyra.

| # | Modul | Bergantung pada | Penulis | Uji jalan | Audit dok | Review alur | Tingkat | Issue |
|---|---|---|---|---|---|---|---|---|
| 1 | Persiapan | — | Pyra | Ursa | Squal | Frieren | beginner | #1 |
| 2 | Cara berpikir ML | Modul 1 | Pyra | Ursa | Squal | Frieren | beginner | #2 |
| 3 | Regresi | Modul 2 | Pyra | Ursa | Squal | Frieren | beginner | #3 |
| 3b | Regularisasi (Ridge dan Lasso) | Modul 3 | Pyra | Ursa | Squal | Frieren | intermediate | #18 |
| 4a | Klasifikasi | Modul 3b | Pyra | Ursa | Squal | Frieren | intermediate | #4 |
| 4b | Pohon dan model gabungan | Modul 4a | Pyra | Ursa | Squal | Frieren | intermediate | #4 |
| 5a | Validasi dan overfitting | Modul 4b | Pyra | Ursa | Squal | Frieren | intermediate | #5 |
| 5b | Metrik penilaian dan ujian Intermediate | Modul 5a | Pyra | Ursa | Squal | Frieren | intermediate | #5 |
| 6a | Rekayasa fitur | Modul 5b | Pyra | Ursa | Squal | Frieren | advanced | #6 |
| 6b | Pipeline | Modul 6a | Pyra | Ursa | Squal | Frieren | advanced | #6 |
| 7 | Tanpa label | Modul 6b | Pyra | Ursa | Squal | Frieren | advanced | #7 |
| 8 | Proyek akhir | Modul 7 | Pyra | Ursa | Squal | Frieren | pro | #8 |

Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas. Iris mengatur urutan dan merge.

Pemecahan modul sudah dilakukan: Pyra menentukan pemecahannya, Iris memperbarui penomoran, dan bagian bernomor huruf mengikuti urutan belajar.

## Kriteria tingkat
Label: `level:beginner`, `level:intermediate`, `level:advanced`, `level:pro`.

| Tingkat | Modul | Kriteria lulus |
|---|---|---|
| beginner | 1–3 | Pembaca bisa menjelaskan dengan kata-katanya sendiri mengapa model diuji pada data yang belum pernah dilihat, dan model dari modul regresi mengalahkan baseline dalam satu proyek mini. |
| intermediate | 3b–5b | Pembaca bisa memilih metrik yang tepat untuk satu kasus dan membuktikan bahwa model tidak sekadar menghafal (overfitting). |
| advanced | 6a–7 | Satu `Pipeline` lengkap dari data mentah sampai hasil, bebas data leakage, dan memberi hasil yang sama setiap kali diulang. |
| pro | 8 | Aplikasi .NET kecil yang memakai model hasil ekspor ONNX: label kelas identik dan probabilitas berada dalam toleransi yang tertulis, dan pembaca bisa menjelaskan keterbatasannya. |

Setiap tingkat ditutup dengan **ujian level** (proyek mini plus beberapa pertanyaan) yang dijalankan Ursa dan diaudit Squal.

_Kriteria dari Frieren._

Modul 8: Toleransi ditulis di dokumen, bukan "sama persis": probabilitas `atol=1e-5` (dibuktikan lewat uji), label kelas harus identik; versi skl2onnx dan onnxruntime dikunci di `uv.lock`, opset ditulis. Menurut cek cepat Pyra (Python 3.14, Linux, opset 22): label kelas identik dan selisih probabilitas maksimum sekitar 6.8e-08. Ini belum diverifikasi tim; `target_opset` dipin secara eksplisit, dan Ursa tetap memverifikasi dari `uv sync` pada lock yang di-commit.

## Fase 2 – Model AI
Tracking: #33. Materi mode cepat modul 9 sampai 15 sudah tertulis di `develop`. Audit dan revisi modul mengikuti issue #33.

| # | Modul | Bergantung pada | Penulis | Uji jalan | Audit dok | Review alur | Issue |
|---|---|---|---|---|---|---|---|
| 9 | Dasar jaringan saraf dan PyTorch | Modul 8 | Pyra | Ursa | Squal | Frieren | #26 |
| 10 | Embedding dan tokenisasi | Modul 9 | Pyra | Ursa | Squal | Frieren | #27 |
| 11 | Transformer | Modul 10 | Pyra | Ursa | Squal | Frieren | #28 |
| 12 | Fine-tune dengan LoRA | Modul 11 | Pyra | Ursa | Squal | Frieren | #29 |
| 13 | Menjalankan model lokal dengan Ollama | Modul 12 | Pyra | Ursa | Squal | Frieren | #30 |
| 14 | RAG (Retrieval-Augmented Generation) | Modul 10, Modul 13 | Pyra | Ursa | Squal | Frieren | #31 |
| 15 | Agen dan proyek akhir Fase 2 | Modul 14 | Pyra | Ursa | Squal | Frieren | #32 |

Aturan Fase 2 (keputusan Frieren):
- Mode cepat CPU wajib lulus dan menjadi gerbang PR. Mode GPU di MyLegion7i opsional dan dinilai dari raw log.
- Data hanya sintetis atau dataset publik dengan sumber dan lisensi jelas. Tanpa data asli perusahaan, termasuk yang sudah disamarkan.
- Unduhan model hanya model kecil berlisensi Apache-2.0 atau MIT: revision HF dipin, safetensors saja, `trust_remote_code=False`. Ollama hanya bind ke `127.0.0.1`.
- Tidak ada adapter, file GGUF, atau indeks di repo maupun HF.
- Modul 13: gabungkan LoRA ke model dasar, konversi ke GGUF dengan llama.cpp, lalu import ke Ollama; pembandingnya model dasar lewat jalur konversi yang sama.
- Modul 15 ditutup dengan proyek akhir RAG plus agen, ditambah bagian singkat .NET lewat HTTP seperti gaya modul 8. Agen hanya memakai tool dari allowlist read-only.
- Merge diblokir hanya untuk sel siswa 16 baris atau lebih.
- Satu SHA, satu laporan audit untuk semua modul. Kriteria berhenti: temuan BLOCK dan Medium nol; Low dan Info dicatat sebagai pertanyaan terbuka.
