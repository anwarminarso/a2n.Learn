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

Modul 8: Toleransi ditulis di dokumen, bukan "sama persis": probabilitas `atol=1e-5` (dibuktikan lewat uji), label kelas harus identik; versi skl2onnx dan onnxruntime dikunci di `uv.lock`, opset ditulis. Menurut cek cepat Pyra (Python 3.14, Linux, opset 22): label kelas identik dan selisih probabilitas maksimum sekitar 1.2e-07. Ini belum diverifikasi tim; `target_opset` dipin secara eksplisit, dan Ursa tetap memverifikasi dari `uv sync` pada lock yang di-commit.

## Fase 2 – Model AI (garis besar, belum ada issue)
1. Dasar jaringan saraf dan PyTorch
2. Transformer
3. Fine-tune dengan LoRA
4. RAG (Retrieval-Augmented Generation)
5. Agen
