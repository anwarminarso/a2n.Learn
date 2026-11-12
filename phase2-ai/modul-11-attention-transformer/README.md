# Modul 11: Transformer

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menghitung attention pada matriks mini, lalu memakai model kecil siap pakai untuk klasifikasi teks, dengan revisi yang dipin dan format safetensors.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Transformer.

## Issue

Modul ini: [#28](https://github.com/anwarminarso/a2n.Learn/issues/28).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 10: Embedding dan tokenisasi](../modul-10-tokenisasi-embedding/).

## Mengapa modul ini

Keputusan tim mengunci modul ini utuh, tanpa folder a/b. Sesi pertama menghitung attention dari nol. Kueri, kunci, dan nilai satu entri karena satu ide. Sesi kedua memakai model pra-latih untuk klasifikasi teks. Kuota sesi kedua masih dua istilah.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. attention
2. kueri, kunci, dan nilai
3. Transformer

### Sesi 2

1. model pra-latih

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

- Sesi 1. Hitung attention dari nol pada matriks mini, lalu beri nama Transformer pada susunan kecil itu.
- Sesi 2. Muat model pra-latih kecil untuk klasifikasi teks. Pin revisi, pakai safetensors, dan setel trust_remote_code=False.
- Ukur pada set uji kecil terhadap baseline kelas yang paling banyak, dengan ambang.

## Rencana latihan

- Pada matriks sangat kecil, periksa bahwa jumlah satu baris bobot perhatian dekat ke 1, dalam ambang.
- Pada beberapa kalimat berlabel dari generator di repo, bandingkan model kecil dengan baseline. Selisih minimal X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Jumlah satu baris bobot perhatian berada di sekitar 1, dengan selisih paling besar X. X belum dipilih.
- Skor klasifikasi pada set uji melebihi baseline minimal X. X belum dipilih.
- Berkas yang dimuat berformat safetensors, dan trust_remote_code=False. Lisensi dicek sebelum unduh.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Matriks mini tanpa unduhan, lalu model sangat kecil untuk beberapa langkah, jalan di CPU.

### mode penuh

Opsional. Kandidat yang lebih besar pada GPU di MyLegion7i. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Kandidat mode cepat: `google/bert_uncased_L-2_H-128_A-2`. Lisensi kartu model Apache-2.0. Berkas `model.safetensors` ada di siblings. `prajjwal1/bert-tiny` tidak dipakai: siblings tidak berisi berkas .safetensors.
- Kandidat mode penuh: `distilbert/distilbert-base-uncased`. Lisensi kartu model Apache-2.0.
- Keduanya model dasar. Kepala klasifikasi dilatih di materi. Placeholder tidak mengklaim model itu sudah bisa mengelompokkan teks.
- Dataset: kalimat berlabel dari generator di repo.
- Status pin: belum dipin. Revisi belum dipilih, jadi lisensi dicek lagi sebelum unduh.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul ini memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
