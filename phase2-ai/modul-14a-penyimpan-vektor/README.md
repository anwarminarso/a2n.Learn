# Modul 14a: Potongan teks dan penyimpan vektor

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa memotong teks, menyimpan vektornya di penyimpan lokal, dan mengambil potongan yang dekat dengan sebuah pertanyaan.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 13: Menjalankan model lokal](../modul-13-model-lokal/). Embedding dari modul 10 dipakai lagi dengan arti yang sudah ada, tanpa entri baru.

## Mengapa modul ini

Memotong, menyimpan, dan mengambil adalah satu sesi duduk. Tiga istilah: potongan, penyimpan vektor, dan pengambilan. Menjawab dengan sumber dan menilai jawaban mengarang dipindah ke modul 14b, karena itu sesi lain dan istilahnya sendiri sudah tiga. Prasyarat urutan adalah modul 13. Konsep yang dipakai datang dari modul 10. Modul ini tidak membutuhkan Ollama. Ketergantungan urutan mengikuti breakdown tim dan bisa ditinjau.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. potongan
2. penyimpan vektor
3. pengambilan

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

- Potong teks menjadi potongan.
- Buat embedding potongan. Arti embedding dari modul 10.
- Simpan vektor di penyimpan lokal.
- Ajukan pertanyaan dan ambil potongan yang dekat.

## Rencana latihan

- Siapkan beberapa dokumen sintetis dari generator di repo.
- Satu pertanyaan yang petunjuknya ada di satu potongan.
- Pengambilan mengembalikan potongan itu, dalam ambang hitungan yang belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Minimal N dari K pertanyaan latihan mengambil potongan yang berisi petunjuk yang diharapkan. N dan K belum dipilih.
- Indeks vektor dari data non-publik tidak masuk repo dan tidak di-push ke Hugging Face.

## Mode cepat dan mode penuh

### mode cepat

Sedikit dokumen, vektor kecil, jalan di CPU.

### mode penuh

Lebih banyak dokumen dan kandidat embedding modul 10, pada GPU bila perlu. Referensi perangkat: laptop RTX 5070 8 GB VRAM.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Dataset: dokumen sintetis dari generator di repo.
- Model embedding: kandidat modul 10, belum dipin.
- Penyimpan: lokal di mesin, bukan layanan luar. Pustaka penyimpan dipilih saat materi ditulis.
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
