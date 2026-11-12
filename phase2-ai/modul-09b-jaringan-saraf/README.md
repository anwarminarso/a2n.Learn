# Modul 9b: Jaringan saraf kecil dan putaran latihan

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa melatih jaringan saraf kecil lewat putaran latihan singkat, lalu membandingkannya dengan model Fase 1 pada data yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 9a: Tensor dan autograd](../modul-09a-tensor-autograd/).

## Mengapa modul ini

Sisa modul 9: jaringan saraf, putaran latihan, dan fungsi aktivasi, lalu perbandingan dengan model Fase 1 pada data yang sama. Jaringan saraf kecil di sini yang dimaksud MLP, yaitu jaringan dengan lapisan di antara masukan dan keluaran. MLP tidak menjadi entri terpisah. PyTorch tetap nama alat, bukan istilah kamus.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. jaringan saraf
2. putaran latihan
3. fungsi aktivasi

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

- Susun jaringan saraf kecil.
- Jalankan putaran latihan singkat.
- Lihat fungsi aktivasi pada contoh angka kecil.
- Bandingkan dengan model Fase 1 pada data yang sama. Pemenang tidak dikunci di placeholder ini.

## Rencana latihan

- Jalankan beberapa langkah putaran latihan pada mode cepat.
- Bandingkan dengan regresi logistik pada data yang sama.
- Catat selisih terhadap baseline dengan ambang, bukan angka persis.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Fungsi kerugian pada data latih turun minimal X setelah beberapa langkah. X belum dipilih. Di bagian Aturan, contoh ambang ini disebut loss. Arti loss tetap fungsi kerugian dari modul 3, bukan istilah baru.
- Pada data uji, jaringan dibanding baseline dan dibanding model Fase 1. Placeholder tidak mengunci model mana yang lebih baik.

## Mode cepat dan mode penuh

### mode cepat

Jaringan sangat kecil, beberapa langkah, jalan di CPU. Data dari iris bawaan scikit-learn atau dari generator di repo.

### mode penuh

Lebih banyak langkah, pada GPU. Referensi perangkat: laptop RTX 5070 8 GB VRAM. Ukuran jaringan mode penuh dipilih saat materi ditulis.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Model Hugging Face: tidak ada. Jaringan ditulis di materi.
- Dataset: iris bawaan scikit-learn, supaya sama dengan kasus Fase 1. Bukan unduhan.
- Pembanding: regresi logistik, arti dari modul 4a.
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
