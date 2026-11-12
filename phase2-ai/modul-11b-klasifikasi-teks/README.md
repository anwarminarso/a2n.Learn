# Modul 11b: Klasifikasi teks dengan model siap pakai

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa memakai model kecil siap pakai dari Hugging Face untuk klasifikasi teks, dengan revisi yang dipin dan format safetensors.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 11a: Attention skala mini](../modul-11a-attention/).

## Mengapa modul ini

Memakai model Hugging Face untuk klasifikasi teks adalah sesi duduk lain, terpisah dari attention yang dihitung dari nol. Istilah yang dikunci sekarang satu, yaitu model pra-latih. Kuota masih dua. Pyra mengisi sisa kuota saat menulis bila perlu, tanpa melewati tiga dan tanpa memecah lagi kecuali istilah barunya lebih dari tiga.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. model pra-latih

Kuota tersisa dua. Pyra boleh menambah paling banyak dua istilah saat menulis, lalu mengunci namanya di kamus. Placeholder ini belum menamai keduanya.

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

- Muat model pra-latih kecil untuk klasifikasi teks.
- Pin revisi, pakai safetensors, dan setel trust_remote_code=False.
- Ukur pada set uji kecil terhadap baseline kelas yang paling banyak, dengan ambang.

## Rencana latihan

- Siapkan beberapa kalimat berlabel dari generator di repo.
- Jalankan mode cepat beberapa langkah di CPU.
- Bandingkan dengan baseline kelas yang paling banyak. Selisih minimal X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Skor pada set uji melebihi baseline minimal X. X belum dipilih.
- Berkas yang dimuat berformat safetensors, dan trust_remote_code=False.

## Mode cepat dan mode penuh

### mode cepat

Model sangat kecil, beberapa langkah, jalan di CPU.

### mode penuh

Model kandidat yang lebih besar, pada GPU. Referensi perangkat: laptop RTX 5070 8 GB VRAM.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Kandidat mode cepat: `prajjwal1/bert-tiny`.
- Kandidat mode penuh: `distilbert/distilbert-base-uncased`.
- Keduanya model dasar. Kepala klasifikasi dilatih di materi pada data yang diizinkan. Placeholder tidak mengklaim model itu sudah bisa mengelompokkan teks.
- Dataset: kalimat berlabel dari generator di repo. Dataset publik hanya dengan persetujuan Frieren atau mas Anwar.
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
