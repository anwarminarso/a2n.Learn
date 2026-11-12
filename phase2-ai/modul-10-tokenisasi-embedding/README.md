# Modul 10: Tokenisasi dan embedding

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa mengubah teks menjadi token lalu vektor, dan membandingkan kemiripan dua teks. Modul ini menjembatani ke modul 11 dan modul 14.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Embedding dan tokenisasi.

## Issue

Modul ini: [#27](https://github.com/anwarminarso/a2n.Learn/issues/27).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 9: PyTorch](../modul-09-pytorch/).

## Mengapa modul ini

Modul ini utuh, satu sesi. Token, embedding, dan kemiripan vektor mengisi kuota tiga. Gambar sebaran sederhana masuk latihan, bukan istilah keempat. Tokenisasi adalah kegiatan membuat token, bukan entri kamus yang lain.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. token
2. embedding
3. kemiripan vektor

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

- Ubah kalimat pendek menjadi token, lalu menjadi vektor embedding.
- Hitung kemiripan vektor dua kalimat dan gambar sebaran sederhana.
- Satu kalimat penutup menunjuk ke modul 11 dan modul 14, tanpa mengisi arti istilah modul itu.

## Rencana latihan

- Siapkan dua kalimat yang dekat artinya dan dua kalimat yang jauh, dari generator di repo.
- Skor kemiripan pasangan yang dekat harus lebih tinggi. Selisih minimal X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Selisih skor kemiripan minimal X. X belum dipilih.
- Mode cepat tidak mengunduh model. Bila mode penuh mengunduh, lisensi sudah dicek sebelum unduh.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Beberapa kalimat sintetis, vektor kecil dari generator di repo, jalan di CPU.

### mode penuh

Opsional. Kandidat embedding di register, pada GPU di MyLegion7i bila diperlukan. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Dataset: kalimat sintetis dari generator di repo.
- Kandidat mode penuh: `sentence-transformers/all-MiniLM-L6-v2`. Lisensi kartu model Apache-2.0, tercatat di register. Status pin: belum dipin.
- Mode cepat tidak wajib memakai model itu.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi yang dipakai 0.40.14. Sejak v0.34.1, pembuatan GGUF dari safetensors memakai perkakas llama.cpp, bukan konverter di dalam Ollama (catatan rilis https://github.com/ollama/ollama/releases/tag/v0.34.1). Jalur yang diajarkan memakai skrip `convert_hf_to_gguf.py` pada llama.cpp tag `b12317`.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
