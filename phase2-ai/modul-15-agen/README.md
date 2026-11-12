# Modul 15: Agen

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menjalankan loop agen yang hanya memanggil alat di allowlist, dan melihat injeksi prompt yang meminta shell atau jaringan ditolak.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 14b: Jawaban dengan sumber](../modul-14b-jawaban-sumber/).

## Mengapa modul ini

Tidak dipecah. Pemanggilan alat, loop agen, dan injeksi prompt mengisi kuota tiga istilah. Batas keamanan ditulis di bagian Aturan, bukan sebagai istilah keempat. Allowlist belum menjadi entri kamus. Latihan injeksi prompt ada di sesi yang sama karena batas itu yang diuji. Prasyarat urutan adalah modul 14b. Loop agen tidak memakai penyimpan vektor. Ketergantungan ini mengikuti urutan breakdown, dan bisa ditinjau bila agen diajarkan tanpa modul 14.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. pemanggilan alat
2. loop agen
3. injeksi prompt

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

- Panggil alat yang ada di allowlist.
- Jalankan loop agen singkat: baca permintaan, panggil alat, baca hasil, lalu jawab.
- Latihan injeksi prompt.
- Alat di luar allowlist, shell bebas, dan jaringan internal ditolak.

## Rencana latihan

- Baca berkas read-only di dalam folder sandbox berhasil untuk berkas yang diizinkan.
- Permintaan yang menyuruh menjalankan shell ditolak.
- Permintaan yang menyuruh membuka jaringan internal ditolak.
- Permintaan yang menyamar tetap terkena allowlist yang sama.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Panggilan di luar allowlist gagal.
- Tidak ada shell bebas, dan tidak ada akses jaringan internal.
- Satu panggilan read-only di dalam folder sandbox berhasil.
- Pengecekan memakai syarat lulus atau gagal, bukan teks jawaban yang persis. Ambang tambahan, bila ada, belum dipilih.

## Mode cepat dan mode penuh

### mode cepat

Loop beberapa langkah, jalan di CPU, tanpa model besar bila memungkinkan.

### mode penuh

Bila loop memakai model untuk memilih alat, pakai kandidat kecil modul 12 pada GPU. Referensi perangkat: laptop RTX 5070 8 GB VRAM.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Model: tidak wajib. Bila dipakai, kandidat modul 12, belum dipin.
- Data: berkas teks sintetis di folder sandbox.
- Alat: baca berkas read-only di folder sandbox saja.
- Status pin: belum dipin.
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
