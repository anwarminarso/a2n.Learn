# Modul 9a: Tensor dan autograd

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menyimpan angka dalam tensor, meminta gradien yang dihitung otomatis, dan membandingkannya dengan hitungan tangan dalam ambang.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 8: Proyek akhir](../../phase1-ml/modul-08-proyek-akhir/). Array dari modul 1 dipakai lagi dengan arti yang sudah ada, tanpa entri baru.

## Mengapa modul ini

Pada breakdown tim, modul 9 mencakup tensor, autograd, jaringan kecil, putaran latihan, dan perbandingan dengan model Fase 1. Itu lebih dari satu sesi duduk dan lebih dari tiga istilah baru. Modul 9a berhenti pada tensor, autograd, dan gradien. PyTorch adalah nama alat, dijelaskan satu kalimat saat materi ditulis, dan belum menjadi entri kamus.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. tensor
2. autograd
3. gradien

## Garis besar bagian

Urutan yang akan ditulis, belum diisi:

1. Cerita pembuka sehari-hari, maksimal satu layar.
2. Teori, maksimal satu halaman, dengan istilah yang direncanakan di atas.
3. Coba sendiri dulu, baru kode.
4. Kasus pada data yang diizinkan di bagian Aturan.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi. Kutipan ditambahkan saat materi ditulis, bukan di placeholder ini.

Notebook, latihan, dan kunci belum dibuat.

Langkah khusus modul ini:

- Buat tensor kecil dari angka yang ditulis tangan.
- Hitung gradien otomatis pada rumus yang sama, lalu bandingkan dengan hitungan tangan.
- Tidak ada model Hugging Face dan tidak ada unduhan.

## Rencana latihan

- Hitung gradien satu rumus kecil dengan tangan, sebelum membuka keluaran kode.
- Bandingkan angka tangan dengan keluaran autograd. Selisih harus di bawah ambang. Angka ambang belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Selisih gradien tangan dan autograd tidak melebihi ambang X. X belum dipilih.
- Mode cepat selesai di CPU tanpa unduhan.

## Mode cepat dan mode penuh

### mode cepat

Tensor sangat kecil, beberapa langkah, jalan di CPU, tanpa unduhan.

### mode penuh

Hitungan yang sama dengan mode cepat. GPU tidak mengubah langkahnya, karena rumusnya kecil. Referensi perangkat mode penuh tetap laptop RTX 5070 8 GB VRAM, supaya gerbang bersama tetap tertulis. Kecocokan kalimat ini dengan aturan mode penuh ditinjau tim: bagian ini belum membutuhkan GPU.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Model Hugging Face: tidak ada.
- Dataset: angka yang ditulis di notebook, bukan unduhan.
- Status pin: belum dipin, karena tidak ada id Hugging Face pada modul ini.
- Lisensi belum dicatat.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data: dataset publik berlisensi jelas atau sintetis dari generator di repo. Tanpa data asli perusahaan.
- Dua mode. Mode cepat memakai model sangat kecil, beberapa langkah, dan jalan di CPU. Mode cepat dipakai untuk gate QA tiap PR. Mode penuh memakai GPU. Referensi perangkat mode penuh: laptop RTX 5070 8 GB VRAM.
- Model dan dataset Hugging Face di-pin ke revisi. Hanya format safetensors. `trust_remote_code=False`. Lisensi tiap model dicatat.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Modul 12 dan modul 14: dataset, adapter LoRA, dan indeks vektor dari data non-publik tidak boleh masuk repo atau di-push ke Hugging Face.
- Modul 13: Ollama mengikat hanya ke 127.0.0.1. Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF lewat skrip llama.cpp `convert_hf_to_gguf.py` wajib.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
