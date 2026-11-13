# Modul 14: RAG (Retrieval-Augmented Generation)

**Tingkat:** —

**Tujuan belajar:** Pembaca bisa memotong teks, menyimpan vektornya, mengambil potongan yang dekat dengan pertanyaan, lalu menyusun jawaban yang menyebut sumber dan menilai jawaban mengarang.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa torch dan tanpa unduhan. Folder indeks dibuat saat notebook jalan dan tidak masuk repo.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): RAG (Retrieval-Augmented Generation).

## Issue

Modul ini: [#31](https://github.com/anwarminarso/a2n.Learn/issues/31).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya pada urutan belajar: [Modul 13: Menjalankan model lokal dengan Ollama](../modul-13-model-lokal/). Embedding dari [Modul 10: Embedding dan tokenisasi](../modul-10-tokenisasi-embedding/) dipakai lagi dengan arti yang sudah ada. Di roadmap, modul ini bergantung pada modul 10 dan modul 13.

## Cerita pembuka

Di laci ada tiga kartu: rak buku, resep dapur, dan jadwal siram kebun. Seseorang bertanya, "kode rak buku cerita". Kamu tidak menjawab dari ingatan. Kamu mencari kartu yang arahnya paling mirip, lalu menulis nomor kartunya di bawah jawaban.

Kalau pertanyaannya tentang harga tiket kereta, dan tidak ada kartunya, kamu bilang catatannya tidak membahas soal itu.

## Teori

Teks latihan ada di folder `dokumen/`. Tiap berkas diawali catatan bahwa isinya teks sintetis. Bukan data asli perusahaan. Mode cepat memotong per baris, membuat vektor dengan `SEED`, lalu menyimpan hasilnya di folder `indeks/`.

### potongan

Satu baris isi pada kartu. Baris catatan di awal berkas tidak ikut. Nama teknisnya **potongan**: sepotong teks pendek dari dokumen yang lebih panjang, supaya tiap ide bisa dicari sendiri.

**Batas analogi:** gunting ini tidak mengubah arti kalimat. Kartu yang terlalu pendek bisa kehilangan siapa yang melakukan apa. Mode cepat memotong per baris, bukan per token model sungguhan.

### penyimpan vektor

Laci yang menyimpan koordinat tiap kartu dan nama berkas asalnya. Nama teknisnya **penyimpan vektor**: tempat menyimpan vektor tiap potongan beserta nama sumbernya. Nama lain untuk tempat ini adalah indeks embedding.

Pada mode cepat, vektor tiap kata diundi dengan `SEED`, lalu vektor kalimat adalah rata-ratanya. Kata yang sama mendapat vektor yang sama. Berkas `potongan.json` ditulis ke folder `indeks/`. Folder itu ada di `.gitignore`.

**Batas analogi:** laci ini bukan model dan bukan jawaban. Indeks dibangun saat notebook jalan dan tidak masuk repo. Koordinat mode cepat bukan vektor model yang diunduh.

### pengambilan

Memilih kartu yang arahnya paling dekat dengan pertanyaan. Nama teknisnya **pengambilan**: memilih potongan yang vektornya paling dekat dengan pertanyaan.

Kedekatan diukur dengan kemiripan vektor dari modul 10, yaitu kosinus. Selain itu dihitung token yang sama antara pertanyaan dan potongan.

**Batas analogi:** dekat di peta bukan berarti isinya menjawab pertanyaan. Bila token bersama kurang dari ambang, kedekatan itu tidak dipakai sebagai sumber.

### RAG

Buka kartu dulu, baru jawab dari kartu itu. Nama teknisnya **RAG**: cara menjawab dengan mengambil potongan dulu, lalu menyusun jawaban dari potongan itu.

Mode cepat menyalin teks potongan. Mode penuh, bila jaringan dinyalakan, boleh memakai model bahasa. Mode cepat tidak menyalakan unduhan itu.

**Batas analogi:** membuka kartu tidak menjamin kalimat jawaban sama persis dengan kartu. Mode penuh yang memakai model tetap bisa menambah kata yang tidak ada di kartu.

### jawaban mengarang

Soal yang tidak punya kartu ditolak, bukan dijawab dengan kartu yang kebetulan agak dekat. Nama teknisnya **jawaban mengarang**: sistem menolak menjawab karena sumbernya tidak cukup. Status pada keluaran adalah `tanpa_sumber`.

Ada tiga ambang, sama dengan kriteria lulus: skor kosinus minimal `0.3`, selisih dengan peringkat kedua minimal `0.15`, dan token bersama minimal `2`. Soal tiket kereta punya token bersama `0` dan skor `0.000000`, jadi statusnya `tanpa_sumber`.

**Batas analogi:** tanda ini bukan bukti seseorang berbohong. Ini tanda pengambilan tidak menemukan sumber yang cukup. Yang dicek ambang, bukan kalimat yang persis.

### kutipan sumber

Nomor kartu yang ditulis di bawah jawaban: nama berkas dan teks potongannya. Nama teknisnya **kutipan sumber**: nama berkas dan teks potongan yang dipakai untuk menopang jawaban.

Pada keluaran, `sumber_rak` adalah `perpustakaan.txt` dan `kutipan_rak` adalah `Kode rak buku cerita adalah B-12.`

**Batas analogi:** nomor kartu menunjukkan asal teks, bukan kebenaran di luar dokumen. Kutipan yang salah pilih tetap sebuah kutipan. Mode cepat menempelkan teks potongan, bukan ringkasan model.

## Coba sendiri dulu, baru kode

Mana kartu yang cocok untuk "kode rak buku cerita": rak perpustakaan, resep jahe, atau siram tomat?

Kalau ditanya harga tiket kereta, kamu mengutip kartu, atau bilang catatannya tidak membahas soal itu?

Jawab dulu. Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

Tiga berkas di `dokumen/`: `dapur.txt`, `kebun.txt`, dan `perpustakaan.txt`. Isinya teks sintetis yang ditulis untuk latihan ini. Bukan data asli perusahaan. Tidak ada unduhan data.

Notebook membaca hanya berkas `.txt` di folder itu, memotong baris isinya, lalu menulis vektor ke `indeks/potongan.json`. Enam potongan tersimpan. Pertanyaan rak mengambil `perpustakaan.txt`. Pertanyaan kereta ditandai jawaban mengarang.

`skor_rak` 0.783885, melewati ambang `0.3`. `selisih_rak` 0.195568, melewati ambang `0.15`. `bagi_rak` 4, melewati ambang `2`.

## Kesalahan yang paling sering terjadi

1. Folder `indeks/` ikut di-commit. Folder itu dibangun saat notebook jalan dan ada di `.gitignore`.
2. Mengambil teks dari luar folder `dokumen/`. Potongan hanya boleh dari berkas yang ada di repo.
3. Menjawab soal jebakan dengan potongan yang kebetulan dekat, padahal token bersamanya nol.
4. Mengunduh model padahal mode cepat tidak mengunduh. Unduhan hanya bila `A2N_UNDUH=1`.
5. Menulis angka di laporan dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Perintah dari root repo:

```bash
uv sync --frozen
uv run pytest
```

Unduhan opsional. Pasang grup torch dulu, karena `transformers` hanya masuk lewat grup itu:

```bash
uv sync --frozen --group torch
A2N_UNDUH=1 uv run pytest phase2-ai/tests/test_modul_09_11.py -k unduh
```

Perintah itu butuh jaringan. Lingkungan yang hanya memakai `uv sync --frozen` tidak memasang `transformers` maupun `huggingface_hub`. Uji `-k unduh` mengunduh model untuk semua modul 10 sampai 15, bukan hanya modul ini. `muat_embedding()` memakai kelas bawaan, yaitu `AutoModel`. `muat_jawaban()` mengirim `AutoModelForCausalLM`.

Sel pertama setiap notebook berisi `SEED = 42`. Tiap sel kode setelah sel pertama memuat satu ide.

## Cek pemahaman

1. Potongan mode cepat dipotong per apa?
2. Mengapa soal tiket kereta tidak mengutip kartu?
3. Pada keluaran, berkas mana yang menjadi kutipan sumber soal rak, dan berapa skornya?

## Kunci jawaban

1. Per baris isi. Baris yang diawali `Catatan:` tidak ikut.
2. Token bersamanya `0` dan skornya `0.000000`, di bawah ambang. Statusnya `tanpa_sumber`.
3. `perpustakaan.txt`. `skor_rak` 0.783885. Kutipannya `Kode rak buku cerita adalah B-12.`

## Sumber

- Lewis, Patrick, et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. <https://arxiv.org/abs/2005.11401>
- Reimers, Nils, and Iryna Gurevych. *Sentence-BERT*. <https://arxiv.org/abs/1908.10084>
- Hugging Face. *AutoModel*. <https://huggingface.co/docs/transformers/en/model_doc/auto>
- NumPy developers. `numpy.linalg.norm`. <https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html>

## Istilah baru

Arti, perumpamaan, dan batas analogi ada di bagian Teori dan di [kamus](../../docs/kamus-istilah.md). Nama di bawah tetap paling banyak tiga per sesi. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. potongan
2. penyimpan vektor
3. pengambilan

### Sesi 2

1. RAG
2. jawaban mengarang
3. kutipan sumber

## Garis besar bagian

1. Cerita pembuka sehari-hari.
2. Teori enam istilah, dibagi dua sesi.
3. Coba sendiri dulu, baru kode.
4. Kasus tiga berkas sintetis, indeks lokal, satu soal bersumber dan satu soal jebakan.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi di bagian Sumber.

Notebook, latihan, dan kunci ada di folder ini. Mode cepat diuji tanpa jaringan dan tanpa torch.

## Rencana latihan

- Satu pertanyaan yang petunjuknya ada di satu potongan. Pengambilan mengembalikan `perpustakaan.txt`.
- Satu soal jebakan yang sumbernya tidak ada. Statusnya `tanpa_sumber`.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Setiap sel siswa 16 baris atau lebih tidak dipakai.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Minimal 1 dari 1 pertanyaan latihan mengambil potongan `perpustakaan.txt`.
- Soal jebakan lulus bila statusnya `tanpa_sumber`.
- Skor soal bersumber minimal `0.3`. Selisih dengan peringkat kedua minimal `0.15`. Token bersama minimal `2`.
- Indeks vektor tidak masuk repo dan tidak di-push ke Hugging Face.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus di CPU, tanpa torch dan tanpa jaringan. Tiga berkas sintetis, vektor numpy dengan `SEED`, indeks di folder `indeks/`.

### mode penuh

Opsional. Embedding `sentence-transformers/all-MiniLM-L6-v2` lewat `AutoModel`, dan model jawaban `HuggingFaceTB/SmolLM2-135M-Instruct` lewat `AutoModelForCausalLM`, hanya bila `A2N_UNDUH=1`. GPU di MyLegion7i dipakai bila model jawaban memerlukannya. Hasil dinilai dari log mentah.

## Model dan dataset

- Dataset: tiga berkas teks sintetis di `dokumen/`. Bukan data asli perusahaan.
- Model embedding: `sentence-transformers/all-MiniLM-L6-v2`. Lisensi Apache-2.0. SHA `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, dicek 2026-11-13. Kelas pemuat: `AutoModel`, karena `muat_embedding()` tidak mengirim kelas.
- Model jawaban: `HuggingFaceTB/SmolLM2-135M-Instruct`. Lisensi Apache-2.0. SHA `12fd25f77366fa6b3b4b768ec3050bf629380bac`, dicek 2026-11-13. Kelas pemuat: `AutoModelForCausalLM`.
- Register: [docs/lisensi-model.md](../../docs/lisensi-model.md).

## Aturan

Aturan ini tetap berlaku pada materi yang sudah ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: revisi yang dipin ada di register.
- Setiap model Hugging Face dimuat dengan `use_safetensors=True` dan `trust_remote_code=False`.
- Unduhan dibatasi lewat `allow_patterns` hanya ke `*.safetensors`, `config.json`, `generation_config.json`, dan berkas tokenizer (`tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `vocab.txt`, `merges.txt`, `vocab.json`). Beberapa repo yang dipakai juga berisi berkas pickle seperti `pytorch_model.bin` atau `training_args.bin`.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul 13 memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.

## Keluaran mode cepat

Angka di bawah disalin dari keluaran `notebook.ipynb` dan `latihan-kunci.ipynb`.

```
berkas_dokumen 3
jumlah_potongan 6
folder_indeks indeks
berkas_indeks potongan.json
vektor_tersimpan 6
status_rak bersumber
sumber_rak perpustakaan.txt
skor_rak 0.783885
bagi_rak 4
kutipan_rak Kode rak buku cerita adalah B-12.
status_jebakan tanpa_sumber
skor_jebakan 0.000000
bagi_jebakan 0
selisih_rak 0.195568
model_embedding sentence-transformers/all-MiniLM-L6-v2
kelas_embedding AutoModel
revisi_embedding 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
model_jawaban HuggingFaceTB/SmolLM2-135M-Instruct
kelas_jawaban AutoModelForCausalLM
revisi_jawaban 12fd25f77366fa6b3b4b768ec3050bf629380bac
unduh False
status_rak_latihan bersumber
sumber_rak_latihan perpustakaan.txt
status_jebakan_latihan tanpa_sumber
```
