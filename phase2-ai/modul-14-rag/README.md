# Modul 14: RAG (Retrieval-Augmented Generation)

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa memotong teks, menyimpan vektornya, mengambil potongan yang dekat dengan pertanyaan, lalu menyusun jawaban yang menyebut sumber dan menilai jawaban mengarang.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): RAG (Retrieval-Augmented Generation).

## Issue

Modul ini: [#31](https://github.com/anwarminarso/a2n.Learn/issues/31).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya pada urutan belajar: [Modul 13: Menjalankan model lokal dengan Ollama](../modul-13-model-lokal/). Embedding dari [Modul 10: Embedding dan tokenisasi](../modul-10-tokenisasi-embedding/) dipakai lagi dengan arti yang sudah ada. Di roadmap, modul ini bergantung pada modul 10 dan modul 13.

## Mengapa modul ini

Keputusan tim mengunci modul ini utuh, tanpa folder a/b. Sesi pertama: potongan, penyimpan vektor, dan pengambilan. Sesi kedua: RAG, jawaban mengarang, dan kutipan sumber. Evaluasi ada di sesi kedua, bukan modul terpisah.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. potongan
2. penyimpan vektor
3. pengambilan

### Sesi 2

1. RAG
2. jawaban mengarang
3. kutipan sumber

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

- Sesi 1. Potong dokumen sintetis, buat embedding, simpan vektor secara lokal, lalu ambil potongan yang dekat dengan pertanyaan.
- Sesi 2. Susun jawaban yang menyebut kutipan sumber.
- Sesi 2 juga menyiapkan soal yang jawabannya tidak ada di dokumen, lalu menilai jawaban mengarang dengan ambang.

## Rencana latihan

- Satu pertanyaan yang petunjuknya ada di satu potongan. Pengambilan mengembalikan potongan itu.
- Satu soal jebakan yang sumbernya tidak ada. Jawaban harus menolak atau ditandai sebagai jawaban mengarang.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Minimal N dari K pertanyaan latihan mengambil potongan yang diharapkan. N dan K belum dipilih.
- Soal jebakan lulus bila ada penolakan atau tanda jawaban mengarang. Bukan dengan kalimat yang persis. Ambang hitungan belum dipilih.
- Indeks vektor tidak masuk repo dan tidak di-push ke Hugging Face.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Sedikit dokumen sintetis, vektor kecil, jalan di CPU.

### mode penuh

Opsional. Lebih banyak dokumen dan kandidat embedding, pada GPU di MyLegion7i bila perlu. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Dataset: dokumen sintetis dari generator di repo.
- Model embedding: kandidat modul 10, belum dipin. Lisensi kartu model Apache-2.0.
- Penyimpan vektor lokal di mesin, bukan layanan luar. Pustaka penyimpan dipilih saat materi ditulis.
- Model jawaban, bila dipakai: kandidat kecil modul 12, belum dipin.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul ini memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
