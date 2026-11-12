# Modul 11a: Attention skala mini

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menghitung attention pada matriks mini dan melihat bobot perhatian pada contoh angka kecil.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 10: Embedding dan tokenisasi](../modul-10-embedding-tokenisasi/).

## Mengapa modul ini

Attention dari nol adalah satu sesi duduk sendiri. Tiga istilah: attention, kueri, kunci, dan nilai sebagai satu entri karena satu ide, serta Transformer. Model siap pakai dipindah ke modul 11b.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. attention
2. kueri, kunci, dan nilai
3. Transformer

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

- Hitung attention dari nol pada matriks mini.
- Perkenalkan kueri, kunci, dan nilai sebagai satu ide.
- Beri nama Transformer pada susunan kecil itu, tanpa memuat model Hugging Face.

## Rencana latihan

- Pakai matriks sangat kecil, misalnya dua baris, dengan angka yang ditulis tangan.
- Periksa bahwa jumlah satu baris bobot perhatian dekat ke 1, dalam ambang.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Jumlah satu baris bobot perhatian berada di sekitar 1, dengan selisih paling besar X. X belum dipilih.
- Mode cepat jalan di CPU tanpa unduhan.

## Mode cepat dan mode penuh

### mode cepat

Matriks mini, beberapa langkah, jalan di CPU, tanpa unduhan.

### mode penuh

Matriks yang sama atau sedikit lebih besar. GPU tidak mengubah langkahnya. Referensi perangkat mode penuh tetap laptop RTX 5070 8 GB VRAM. Sama seperti modul 9a, kebutuhan GPU pada bagian ini ditinjau tim.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Model Hugging Face: tidak ada.
- Dataset: angka matriks yang ditulis di notebook, bukan unduhan.
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
