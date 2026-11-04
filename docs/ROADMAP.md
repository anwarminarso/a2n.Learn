# Roadmap

Aturan data: Default semua modul: dataset bawaan scikit-learn atau data sintetis dari generator di repo, tanpa unduhan. Data publik hanya pengecualian: sumber dan lisensi jelas, salinan kecil di repo, dan harus disetujui Frieren atau mas Anwar dulu. Modul 8 memakai data sintetis ala tambang. Tanpa data ANTAM.

Istilah yang dipakai di semua modul dicatat di [kamus-istilah.md](kamus-istilah.md).

## Fase 1 – Machine Learning
Urutan wajib: modul berikutnya baru dimulai setelah modul sebelumnya lolos Ursa (PASS) dan Squal (PASS / PASS BERSYARAT). Modul 1 dikerjakan pertama oleh Pyra.

| # | Modul | Bergantung pada | Penulis | Uji jalan | Audit dok | Review alur | Tingkat | Issue |
|---|---|---|---|---|---|---|---|---|
| 1 | Persiapan | — | Pyra | Ursa | Squal | Frieren | beginner | #1 |
| 2 | Cara berpikir ML | Modul 1 | Pyra | Ursa | Squal | Frieren | beginner | #2 |
| 3 | Regresi | Modul 2 | Pyra | Ursa | Squal | Frieren | beginner | #3 |
| 4 | Klasifikasi | Modul 3 | Pyra | Ursa | Squal | Frieren | intermediate | #4 |
| 5 | Evaluasi | Modul 4 | Pyra | Ursa | Squal | Frieren | intermediate | #5 |
| 6 | Rekayasa fitur dan Pipeline | Modul 5 | Pyra | Ursa | Squal | Frieren | advanced | #6 |
| 7 | Tanpa label | Modul 6 | Pyra | Ursa | Squal | Frieren | advanced | #7 |
| 8 | Proyek akhir | Modul 7 | Pyra | Ursa | Squal | Frieren | pro | #8 |

Satu modul cukup untuk satu sesi duduk; jadwal mingguan menunggu keputusan mas. Iris mengatur urutan dan merge.

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

Modul 8: Toleransi ditulis di dokumen, bukan "sama persis": probabilitas `atol=1e-5` (dibuktikan lewat uji), label kelas harus identik; versi skl2onnx, onnxruntime, dan opset dikunci dan ditulis.

## Fase 2 – Model AI (garis besar, belum ada issue)
1. Dasar jaringan saraf dan PyTorch
2. Transformer
3. Fine-tune dengan LoRA
4. RAG (Retrieval-Augmented Generation)
5. Agen
