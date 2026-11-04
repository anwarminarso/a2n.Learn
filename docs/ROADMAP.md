# Roadmap

## Fase 1 – Machine Learning
Urutan wajib: modul berikutnya baru dimulai setelah modul sebelumnya lolos Ursa (PASS) dan Squal (PASS / PASS BERSYARAT). Modul 1 dikerjakan pertama oleh Pyra.

| # | Modul | Bergantung pada | Penulis | Uji jalan | Audit dok | Review alur | Tingkat | Estimasi | Issue |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Persiapan | — | Pyra | Ursa | Squal | Frieren | beginner | 1 minggu | #1 |
| 2 | Cara berpikir ML | Modul 1 | Pyra | Ursa | Squal | Frieren | beginner | 1 minggu | #2 |
| 3 | Regresi | Modul 2 | Pyra | Ursa | Squal | Frieren | beginner | 1 minggu | #3 |
| 4 | Klasifikasi | Modul 3 | Pyra | Ursa | Squal | Frieren | intermediate | 1 minggu | #4 |
| 5 | Evaluasi | Modul 4 | Pyra | Ursa | Squal | Frieren | intermediate | 1 minggu | #5 |
| 6 | Rekayasa fitur dan Pipeline | Modul 5 | Pyra | Ursa | Squal | Frieren | advanced | 1 minggu | #6 |
| 7 | Tanpa label | Modul 6 | Pyra | Ursa | Squal | Frieren | advanced | 1 minggu | #7 |
| 8 | Proyek akhir | Modul 7 | Pyra | Ursa | Squal | Frieren | pro | 1 minggu | #8 |

Estimasi 1 minggu per modul, dapat dipadatkan sesuai jam per minggu yang mas pilih. Iris mengatur urutan dan merge.

## Kriteria tingkat
Label: `level:beginner`, `level:intermediate`, `level:advanced`, `level:pro`.

| Tingkat | Modul | Kriteria lulus |
|---|---|---|
| beginner | 1–3 | Pembaca bisa menjelaskan dengan kata-katanya sendiri mengapa model diuji pada data yang belum pernah dilihat, dan model dari modul regresi mengalahkan baseline dalam satu proyek mini. |
| intermediate | 4–5 | Pembaca bisa memilih metrik yang tepat untuk satu kasus dan membuktikan bahwa model tidak sekadar menghafal (overfitting). |
| advanced | 6–7 | Satu `Pipeline` lengkap dari data mentah sampai hasil, bebas data leakage, dan memberi hasil yang sama setiap kali diulang. |
| pro | 8 | Aplikasi .NET kecil yang memakai model hasil ekspor ONNX: label kelas identik dan probabilitas berada dalam toleransi yang tertulis, dan pembaca bisa menjelaskan keterbatasannya. |

Setiap tingkat ditutup dengan **ujian level** (proyek mini plus beberapa pertanyaan) yang dijalankan Ursa dan diaudit Squal.

_Kriteria dari Frieren._

## Fase 2 – Model AI (garis besar, belum ada issue)
1. Dasar jaringan saraf dan PyTorch
2. Transformer
3. Fine-tune dengan LoRA
4. RAG (Retrieval-Augmented Generation)
5. Agen
