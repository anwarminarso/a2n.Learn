# Modul 10: Embedding dan tokenisasi

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa mengubah teks menjadi token lalu vektor, dan membandingkan kemiripan dua teks. Modul ini menjembatani ke modul 11 dan modul 14 tanpa mengajarkan isi kedua modul itu.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 9b: Jaringan saraf kecil dan putaran latihan](../modul-09b-jaringan-saraf/).

## Mengapa modul ini

Tidak dipecah. Token, embedding, dan kemiripan vektor muat satu sesi duduk. Gambar sebaran sederhana masuk rencana latihan, bukan istilah keempat. Tokenisasi adalah kegiatan membuat token, bukan entri kamus yang lain.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. token
2. embedding
3. kemiripan vektor

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

- Ubah kalimat pendek menjadi token.
- Ubah token menjadi vektor embedding.
- Hitung kemiripan vektor dua kalimat.
- Gambar sebaran sederhana untuk beberapa kalimat.
- Satu kalimat penutup menunjuk ke modul 11 dan modul 14, tanpa mengisi arti istilah modul itu.

## Rencana latihan

- Siapkan dua kalimat yang dekat artinya dan dua kalimat yang jauh, dari generator di repo.
- Skor kemiripan pasangan yang dekat harus lebih tinggi, dengan selisih minimal X. X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Selisih skor kemiripan minimal X. X belum dipilih.
- Mode cepat tidak mengunduh model.

## Mode cepat dan mode penuh

### mode cepat

Beberapa kalimat sintetis, vektor kecil dari generator di repo, jalan di CPU.

### mode penuh

Model embedding kandidat di bawah, pada GPU bila model itu memerlukannya. Referensi perangkat: laptop RTX 5070 8 GB VRAM.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Dataset: kalimat sintetis dari generator di repo.
- Model mode penuh: `sentence-transformers/all-MiniLM-L6-v2`.
- Model mode cepat: tidak wajib memakai model itu.
- Status pin: belum dipin.
- Lisensi belum dicatat. Jangan menyalin lisensi dari ingatan.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data: dataset publik berlisensi jelas atau sintetis dari generator di repo. Tanpa data asli perusahaan.
- Dua mode. Mode cepat memakai model sangat kecil, beberapa langkah, dan jalan di CPU. Mode cepat dipakai untuk gate QA tiap PR. Mode penuh memakai GPU. Referensi perangkat mode penuh: laptop RTX 5070 8 GB VRAM.
- Model dan dataset Hugging Face di-pin ke revisi. Hanya format safetensors. `trust_remote_code=False`. Lisensi tiap model dicatat.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Modul 12 dan modul 14: dataset, adapter LoRA, dan indeks vektor dari data non-publik tidak boleh masuk repo atau di-push ke Hugging Face.
- Modul 13: Ollama mengikat hanya ke 127.0.0.1. Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF lewat skrip llama.cpp `convert_hf_to_gguf.py` wajib.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
