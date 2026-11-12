# Modul 15: Agen dan proyek akhir Fase 2

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menjalankan loop agen yang hanya memanggil alat di allowlist, menutup Fase 2 dengan proyek kecil RAG plus agen, dan memanggil hasilnya dari program .NET lewat HTTP dengan pola yang sama seperti modul 8.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Agen dan proyek akhir Fase 2.

## Issue

Modul ini: [#32](https://github.com/anwarminarso/a2n.Learn/issues/32).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 14: RAG (Retrieval-Augmented Generation)](../modul-14-rag/). Di roadmap, modul ini bergantung pada modul 14. Peladen lokal dari [Modul 13: Menjalankan model lokal dengan Ollama](../modul-13-model-lokal/) dan kandidat model dari [Modul 12: Fine-tune dengan LoRA](../modul-12-lora/) dipakai lagi dengan arti yang sudah ada.

## Mengapa modul ini

Modul ini utuh. Sesi pertama mengunci pemanggilan alat, loop agen, dan injeksi prompt. Allowlist belum menjadi entri kamus. Sesi kedua adalah proyek akhir: RAG dari modul 14 ditambah loop agen, plus bagian singkat program .NET. Panggilan itu HTTP ke 127.0.0.1, mengikuti pola modul 8 yang berupa program kecil, batas angka yang tertulis, dan penjelasan keterbatasan. Inferensi dari modul 8 dipakai lagi. HTTP bukan istilah baru.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. pemanggilan alat
2. loop agen
3. injeksi prompt

### Sesi 2

Tidak ada istilah baru pada sesi ini.

## Garis besar bagian

Urutan yang akan ditulis, belum diisi:

1. Cerita pembuka sehari-hari, maksimal satu layar.
2. Teori, dengan istilah sesi yang sedang dibaca.
3. Coba sendiri dulu, baru kode.
4. Kasus pada data yang diizinkan di bagian Aturan.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi. Kutipan ditambahkan saat materi ditulis, bukan di placeholder ini.

Notebook, latihan, dan kunci belum dibuat.

Sesi di dalam modul ini, bukan folder terpisah:

- Sesi 1. Panggil alat di allowlist, jalankan loop agen singkat, lalu latihan injeksi prompt.
- Alat di luar allowlist, shell bebas, dan jaringan internal ditolak.
- Sesi 2. Proyek akhir menggabungkan RAG dan agen pada dokumen sintetis.
- Bagian singkat .NET: program kecil memanggil peladen lokal lewat HTTP di 127.0.0.1, bukan lewat berkas ONNX. Bentuknya mengikuti modul 8: satu panggilan, batas yang tertulis, dan keterbatasan yang dijelaskan.

## Rencana latihan

- Baca berkas read-only di dalam folder sandbox berhasil untuk berkas yang diizinkan.
- Permintaan yang menyuruh menjalankan shell ditolak. Permintaan yang menyuruh membuka jaringan internal ditolak.
- Path `../`, path absolut, dan symlink yang keluar dari folder sandbox ditolak.
- Pada proyek akhir, satu pertanyaan dijawab dengan kutipan sumber, dan satu injeksi prompt gagal di luar allowlist.
- Sketsa panggilan HTTP dari .NET hanya menunjukkan alamat 127.0.0.1 dan satu batas ambang. Kode panjang belum ditulis.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Panggilan di luar allowlist gagal. Tidak ada shell bebas, dan tidak ada akses jaringan internal.
- Path traversal ditolak: `../`, path absolut, dan symlink yang keluar dari folder sandbox.
- Satu panggilan read-only di dalam folder sandbox berhasil.
- Proyek akhir memakai RAG dan agen pada data sintetis. Jawaban bersumber lulus dengan ambang, bukan teks persis. Ambang belum dipilih.
- Bagian .NET menyebut HTTP ke 127.0.0.1 dan satu batas yang tertulis, mengikuti pola modul 8.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Loop beberapa langkah, jalan di CPU, tanpa model besar bila memungkinkan.

### mode penuh

Opsional. Bila loop memakai model untuk memilih alat, pakai kandidat kecil modul 12 pada GPU di MyLegion7i. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Model: tidak wajib. Bila dipakai, kandidat modul 12, belum dipin. Lisensi mengikuti register.
- Data proyek akhir: berkas teks sintetis di folder sandbox, plus dokumen sintetis dari modul 14.
- Alat: baca berkas read-only di folder sandbox saja.
- Panggilan .NET hanya ke 127.0.0.1.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Teramati pada Ollama 0.40.14 di Windows: impor safetensors gagal dengan pesan yang meminta runtime MLX. Ini catatan pengamatan pada versi itu. Jalur yang diajarkan memakai skrip `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
