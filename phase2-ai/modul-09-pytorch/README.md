# Modul 9: Dasar jaringan saraf dan PyTorch

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menyimpan angka dalam tensor, memeriksa gradien yang dihitung otomatis, lalu melatih jaringan saraf pertama dan membandingkannya dengan model Fase 1 pada data yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Dasar jaringan saraf dan PyTorch.

## Issue

Modul ini: [#26](https://github.com/anwarminarso/a2n.Learn/issues/26).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 8: Proyek akhir](../../phase1-ml/modul-08-proyek-akhir/). Array dari modul 1 dipakai lagi dengan arti yang sudah ada.

## Mengapa modul ini

Keputusan tim mengunci modul ini utuh, tanpa folder a/b. Di dalam halaman ini ada dua sesi. Sesi pertama berhenti pada tensor, autograd, dan gradien. Sesi kedua memakai jaringan saraf, putaran latihan, dan fungsi aktivasi. Jaringan saraf pertama di sini yang dimaksud MLP, yaitu jaringan dengan lapisan di antara masukan dan keluaran. MLP tidak menjadi entri terpisah. PyTorch adalah nama alat, bukan istilah kamus.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. tensor
2. autograd
3. gradien

### Sesi 2

1. jaringan saraf
2. putaran latihan
3. fungsi aktivasi

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

- Sesi 1. Buat tensor kecil dari angka yang ditulis tangan, lalu bandingkan gradien otomatis dengan hitungan tangan.
- Sesi 2. Latih jaringan saraf pertama dengan putaran latihan singkat, pada data yang sama dengan model Fase 1. Pemenang tidak dikunci di placeholder ini.

## Rencana latihan

- Hitung gradien satu rumus kecil dengan tangan, sebelum membuka keluaran kode.
- Jalankan beberapa langkah putaran latihan pada mode cepat, lalu bandingkan dengan regresi logistik pada data yang sama.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Selisih gradien tangan dan autograd tidak melebihi ambang X. X belum dipilih.
- Fungsi kerugian pada data latih turun minimal X setelah beberapa langkah. X belum dipilih. Di bagian Aturan, contoh ambang ini disebut loss. Arti loss tetap fungsi kerugian dari modul 3.
- Pada data uji, jaringan dibanding baseline dan dibanding model Fase 1. Placeholder tidak mengunci model mana yang lebih baik.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Tensor dan jaringan sangat kecil, beberapa langkah, jalan di CPU, tanpa unduhan. Ini gerbang tiap PR.

### mode penuh

Opsional. Lebih banyak langkah pada GPU di MyLegion7i. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Model Hugging Face: tidak ada. Jaringan ditulis di materi.
- Dataset: iris bawaan scikit-learn, supaya sama dengan kasus Fase 1. Bukan unduhan. Bukan data asli perusahaan.
- Pembanding: regresi logistik, arti dari modul 4a.
- Status pin: belum dipin, karena tidak ada id yang diunduh.
- Lisensi kartu model tidak berlaku di modul ini. Register: [docs/lisensi-model.md](../../docs/lisensi-model.md).

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul ini memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
