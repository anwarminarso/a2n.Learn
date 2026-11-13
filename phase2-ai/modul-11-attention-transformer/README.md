# Modul 11: Transformer

**Tingkat:** —

**Tujuan belajar:** Pembaca bisa menghitung attention pada matriks mini, lalu memakai model kecil untuk klasifikasi teks. Revisi model yang diunduh dipin, dan bobot yang dimuat berformat safetensors.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa unduhan.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Transformer.

## Issue

Modul ini: [#28](https://github.com/anwarminarso/a2n.Learn/issues/28).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 10: Embedding dan tokenisasi](../modul-10-tokenisasi-embedding/). Token dan embedding dipakai lagi dengan arti yang sudah ada.

## Cerita pembuka

Kamu membaca satu kata di tengah kalimat, lalu menoleh ke kata lain. Perhatianmu terbagi. Seluruh bagian itu, kalau dijumlahkan, habis menjadi satu. Tidak ada sisa perhatian yang mengambang, dan tidak ada bagian yang minus.

Rumus attention melakukan hal yang mirip pada angka, bukan pada niat orang. Modul ini menghitungnya pada matriks mini, lalu melatih model kecil pada delapan kalimat sintetis. Model yang bobotnya sudah dilatih orang lain disiapkan untuk mode penuh, dan mode cepat tidak mengunduhnya.

## Teori

Softmax, yaitu fungsi yang mengubah skor menjadi bobot positif yang berjumlah satu, dijelaskan satu kalimat dan belum menjadi entri kamus. Delapan kalimat dan labelnya ditulis di notebook. Bukan data asli perusahaan.

### attention

Tiga token punya kueri dan kunci berukuran dua. Skornya perkalian, dibagi akar dua, lalu softmax. Jumlah satu baris bobot dibanding 1. Selisih terbesar pada keluaran adalah 0. Nama teknisnya **attention**: bobot yang menunjukkan seberapa besar satu token menoleh ke token lain. Jumlah bobot pada satu baris dekat ke 1.

**Batas analogi:** bobot ini hasil rumus, bukan niat manusia. Menoleh bukan berarti memahami. Satu baris yang jumlahnya 1 tidak membuktikan tebakan kelas benar.

### kueri, kunci, dan nilai

Tiga peran pada tiap token, satu ide. Kueri bertanya, kunci menawarkan kecocokan, nilai adalah isi yang dijumlahkan setelah bobot ada. Pada notebook, nilai `v` dikalikan bobot menjadi `campuran` berbentuk `(3, 2)`. Nama teknisnya **kueri, kunci, dan nilai**.

Bayangkan perpustakaan: pertanyaanmu dicocokkan dengan label rak, lalu kamu membawa isi buku sesuai kecocokan itu.

**Batas analogi:** yang dicocokkan adalah perkalian angka, bukan petugas yang paham pertanyaan. Label rak bukan arti kalimat. Isi yang dibawa masih vektor, bukan kalimat jawaban.

### Transformer

Di mode cepat ada dua bagian terpisah: satu blok attention, dan classifier yang tidak memakai keluaran attention. Classifier di notebook adalah regresi logistik bag-of-tokens, bukan Transformer. Nama teknisnya **Transformer**: susunan yang memakai attention untuk mencampur token, lalu lapisan kecil menghasilkan tebakan.

**Batas analogi:** satu blok pada matriks mini bukan model obrolan besar. Menyusun blok itu tidak otomatis membuat klasifikasi benar. Model pra-latih yang besar juga Transformer, tetapi bobotnya tidak disalin ke repo ini.

### model pra-latih

Adonan roti yang sudah diulen orang lain bisa dipanggang untuk hidangan hari ini. Nama teknisnya **model pra-latih**: model yang bobotnya sudah dilatih pada data lain, lalu kita pakai atau latih lagi.

Mode penuh memakai `google/bert_uncased_L-2_H-128_A-2` pada revisi `30b0a37ccaaa32f332884b96992754e246e48c5f`. Mode opsional yang lebih besar memakai `distilbert/distilbert-base-uncased` pada revisi `12040accade4e8a0f71eabdb258fecc2e7e948be`. Keduanya model dasar. Kepala klasifikasi di mode cepat dilatih di notebook, dari bobot nol, bukan dari kartu model.

`prajjwal1/bert-tiny` tidak dipakai. `siblings` reponya tidak berisi berkas `.safetensors`.

**Batas analogi:** adonan itu dilatih pada teks publik, bukan pada delapan kalimat modul ini. Kepala kelas yang kita latih di mode cepat mulai dari nol. Kita mengunci revisi dan hanya memuat safetensors. Mode cepat tidak mengunduh adonan itu, karena mode cepat tidak punya jaringan.

## Coba sendiri dulu, baru kode

Satu baris bobot `0.2`, `0.3`, dan `0.5`. Jumlahnya berapa?

Jawab dulu. Lalu jalankan `notebook.ipynb` dari sel pertama.

## Kasus nyata

Delapan kalimat sintetis: empat tentang kucing (label 1) dan empat tentang cuaca (label 0). Lima baris menjadi data latih, indeks `0, 1, 3, 4, 6`. Tiga baris menjadi data uji, indeks `2, 5, 7`. Tidak ada unduhan. Bukan data asli perusahaan.

Baseline data uji selalu menebak label 1, karena label 1 lebih banyak di data latih. Salah baseline pada data uji adalah 2. Model kecil setelah 30 langkah salah 0. Selisihnya 2, melewati ambang 1.

Fungsi kerugian di awal 0.25, karena tebakan awal 0.5 pada label 0 atau 1. Setelah 30 langkah, fungsi kerugian pada data latih 0.008027.

Pemuat mode penuh ada di `muat.py`. Setiap panggilan mengirim `revision` dari register, `use_safetensors=True`, `trust_remote_code=False`, dan `allow_patterns` pada bagian Aturan. Panggilannya tidak dijalankan saat `A2N_UNDUH` mati.

## Kesalahan yang paling sering terjadi

1. Jumlah baris bobot yang 0.6 dianggap cukup dekat ke 1. Ambang modul ini `0.000001`. Latihan yang jumlahnya 0.6 ditolak.
2. Baseline dihitung dari data uji, bukan dari data latih. Notebook memakai kelas yang paling banyak di data latih.
3. Mode cepat dianggap mengunduh BERT kecil. Mode cepat tidak mengunduh. BERT kecil adalah mode penuh.
4. `prajjwal1/bert-tiny` dipakai karena kartunya bertulis MIT. Berkas safetensors-nya tidak ada, jadi id itu ditolak.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Dari root repo:

```bash
uv sync --frozen
uv run pytest
```

Unduhan opsional. Pasang grup torch dulu, karena `transformers` hanya masuk lewat grup itu:

```bash
uv sync --frozen --group torch
A2N_UNDUH=1 uv run pytest phase2-ai/tests/test_modul_09_11.py -k unduh
```

Perintah itu butuh jaringan. Lingkungan yang hanya memakai `uv sync --frozen` tidak memasang `transformers` maupun `huggingface_hub`. Uji `-k unduh` mengunduh model untuk semua modul 10 sampai 15, bukan hanya modul ini.

## Cek pemahaman

1. Mengapa jumlah satu baris bobot perhatian dekat ke 1?
2. Kueri, kunci, dan nilai satu entri atau tiga entri?
3. Pada keluaran, salah uji model lebih kecil daripada baseline minimal 1, atau tidak?

## Kunci jawaban

1. Softmax membuat bobot positif yang dijumlahkan menjadi satu. Selisih pada matriks mini adalah 0.
2. Satu entri, karena tiga peran itu satu ide.
3. Lebih kecil. `salah_uji_model` 0 dan `salah_uji_baseline` 2. Selisihnya 2.

## Sumber

- Vaswani, Ashish, dkk. *Attention Is All You Need*. <https://arxiv.org/abs/1706.03762>
- Hugging Face. `from_pretrained`. <https://huggingface.co/docs/transformers/main/en/main_classes/model#transformers.PreTrainedModel.from_pretrained>
- Hugging Face. *BERT*. <https://huggingface.co/docs/transformers/model_doc/bert>

## Istilah baru

Arti, perumpamaan, dan batas analogi ada di bagian Teori dan di [kamus](../../docs/kamus-istilah.md). Sesi kedua hanya satu istilah. Sisa kuota tidak diisi.

### Sesi 1

1. attention
2. kueri, kunci, dan nilai
3. Transformer

### Sesi 2

1. model pra-latih

## Garis besar bagian

1. Cerita pembuka.
2. Teori attention, lalu model pra-latih.
3. Coba sendiri dulu, baru kode.
4. Delapan kalimat sintetis dan baseline.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi.

## Rencana latihan

- Jumlahkan baris `0.2`, `0.3`, `0.5`.
- Tolak baris `0.2`, `0.2`, `0.2` karena jumlahnya jauh dari 1.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Setiap sel di notebook siswa paling banyak 15 baris.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Selisih jumlah satu baris bobot perhatian dari 1 paling besar `0.000001`.
- Salah klasifikasi pada data uji lebih kecil daripada baseline, selisih minimal 1.
- Berkas yang dimuat memakai `use_safetensors=True`, dan trust_remote_code=False. Lisensi dicek sebelum unduh. Revisi yang dipin ada di register.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Matriks mini tanpa unduhan, lalu model sangat kecil untuk 30 langkah, jalan di CPU.

### mode penuh

Opsional. `google/bert_uncased_L-2_H-128_A-2` pada revisi yang dipin. Model yang lebih besar, `distilbert/distilbert-base-uncased`, juga opsional. GPU di MyLegion7i dipakai bila mesin itu memakainya. Hasil dinilai dari log mentah.

## Model dan dataset

- Mode penuh: `google/bert_uncased_L-2_H-128_A-2`. Lisensi Apache-2.0. SHA `30b0a37ccaaa32f332884b96992754e246e48c5f`, dicek 2026-11-13. Berkas `model.safetensors` ada. Repo ini juga berisi pickle `pytorch_model.bin`. Muat dengan `use_safetensors=True` agar pemuat tidak jatuh ke format pickle.
- Opsional yang lebih besar: `distilbert/distilbert-base-uncased`. Lisensi Apache-2.0. SHA `12040accade4e8a0f71eabdb258fecc2e7e948be`. Berkas `model.safetensors` ada. Repo ini juga berisi `pytorch_model.bin`.
- `prajjwal1/bert-tiny` tidak dipakai: siblings tidak berisi berkas .safetensors.
- Keduanya model dasar. Kepala klasifikasi mode cepat dilatih di materi, dari nol.
- Dataset: kalimat berlabel yang ditulis di notebook.
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
selisih_jumlah 0.0
bentuk_campuran (3, 2)
banyak 8
kolom 16
kerugian_awal 0.25
kerugian_akhir 0.008027
salah_uji_model 0
salah_uji_baseline 2
model_penuh google/bert_uncased_L-2_H-128_A-2
revisi_penuh 30b0a37ccaaa32f332884b96992754e246e48c5f
model_opsional distilbert/distilbert-base-uncased
revisi_opsional 12040accade4e8a0f71eabdb258fecc2e7e948be
unduh False
jumlah_baris 1.0
jumlah_salah 0.6
```
