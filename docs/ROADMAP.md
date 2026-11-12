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

Urutan wajib sama seperti Fase 1: modul berikutnya baru dimulai setelah modul sebelumnya lolos Ursa (PASS) dan Squal (PASS / PASS BERSYARAT). Isi materi belum ditulis. Berkas di `phase2-ai/` berstatus PLACEHOLDER. Audit dan revisi menyusul setelah semua placeholder ada. Issue dibuat terpisah oleh PM, jadi kolom Issue berisi —.

Satu modul cukup untuk satu sesi duduk. Pemecahan mengikuti batas Fase 1: paling banyak tiga istilah baru per modul.

| # | Modul | Bergantung pada | Penulis | Uji jalan | Audit dok | Review alur | Tingkat | Issue |
|---|---|---|---|---|---|---|---|---|
| 9a | Tensor dan autograd | Modul 8 | Pyra | Ursa | Squal | Frieren | pro | — |
| 9b | Jaringan saraf kecil dan putaran latihan | Modul 9a | Pyra | Ursa | Squal | Frieren | pro | — |
| 10 | Embedding dan tokenisasi | Modul 9b | Pyra | Ursa | Squal | Frieren | pro | — |
| 11a | Attention skala mini | Modul 10 | Pyra | Ursa | Squal | Frieren | pro | — |
| 11b | Klasifikasi teks dengan model siap pakai | Modul 11a | Pyra | Ursa | Squal | Frieren | pro | — |
| 12 | Penyelarasan dengan LoRA | Modul 11b | Pyra | Ursa | Squal | Frieren | pro | — |
| 13 | Menjalankan model lokal | Modul 12 | Pyra | Ursa | Squal | Frieren | pro | — |
| 14a | Potongan teks dan penyimpan vektor | Modul 13 | Pyra | Ursa | Squal | Frieren | pro | — |
| 14b | Jawaban dengan sumber | Modul 14a | Pyra | Ursa | Squal | Frieren | pro | — |
| 15 | Agen | Modul 14b | Pyra | Ursa | Squal | Frieren | pro | — |

Pemecahan: modul 9 menjadi 9a (tensor, autograd, gradien) dan 9b (jaringan saraf, putaran latihan, fungsi aktivasi) karena satu sesi tidak muat dari tensor sampai perbandingan dengan model Fase 1, dan istilahnya lebih dari tiga. Modul 11 menjadi 11a (attention dari nol) dan 11b (model Hugging Face untuk klasifikasi teks) karena dua kegiatan itu dua sesi. Modul 14 menjadi 14a (potongan, penyimpan vektor, pengambilan) dan 14b (RAG, jawaban mengarang, kutipan sumber) karena menyusun penyimpan dan menilai jawaban mengarang adalah dua sesi, dan istilahnya lebih dari tiga.

Tidak dipecah: modul 10 (token, embedding, kemiripan vektor) satu sesi. Modul 12 (penyelarasan, LoRA, adapter) satu sesi pada mode cepat; mengukur sebelum dan sesudah memakai set uji yang sama. Modul 13 (GGUF, penggabungan adapter, peladen lokal) satu sesi, satu jalur konversi untuk model dengan LoRA dan kontrol tanpa LoRA. Modul 15 (pemanggilan alat, loop agen, injeksi prompt) satu sesi; batas keamanan ada di bagian Aturan, bukan istilah keempat.

Tingkat semua modul Fase 2 adalah pro. Tingkat tidak diturunkan setelah modul 8, dan tidak ada label tingkat baru. Baris pro pada tabel kriteria tingkat di atas tetap milik modul 8. Kriteria lulus tiap modul Fase 2 berstatus DRAF di README modul itu.

Mode cepat (model sangat kecil, beberapa langkah, CPU) adalah gate QA tiap PR. Mode penuh memakai GPU. Referensi perangkat mode penuh: laptop RTX 5070 8 GB VRAM. Pada modul 9a dan 11a, hitungannya kecil sehingga mode penuh tidak menambah kerja GPU. Kalimat itu ditinjau tim.

Aturan data Fase 2, selain aturan data di awal dokumen ini: dataset publik berlisensi jelas atau sintetis dari generator di repo. Tanpa data asli perusahaan. Model dan dataset Hugging Face di-pin ke revisi, hanya format safetensors, `trust_remote_code=False`, dan lisensi tiap model dicatat. Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis. Dataset, adapter LoRA, dan indeks vektor dari data non-publik tidak boleh masuk repo atau di-push ke Hugging Face. Ollama mengikat hanya ke 127.0.0.1. Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF lewat `convert_hf_to_gguf.py` wajib. Tools agen hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.

Keputusan placeholder yang perlu ditinjau tim:

- Semua modul bertingkat pro, tanpa label baru.
- Yang dipecah: 9, 11, dan 14. Yang utuh: 10, 12, 13, dan 15.
- Modul 14a bergantung urutan pada modul 13, tetapi konsepnya dari modul 10 dan tidak memakai Ollama. Modul 15 bergantung urutan pada modul 14b, tetapi loop agen tidak memakai penyimpan vektor.
- Modul 11b mengunci satu istilah dan menyisakan kuota dua.
- PyTorch, fine-tune, Ollama, dan allowlist belum menjadi entri kamus.
- Kandidat model belum dipin. Lisensi belum dicatat.
- Notebook belum dibuat. Template issue dan dokumen kontribusi belum diubah.
- Peran penulis, uji jalan, audit, dan review alur disalin dari Fase 1.
