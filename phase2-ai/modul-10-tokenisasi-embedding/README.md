# Modul 10: Embedding dan tokenisasi

**Tingkat:** —

**Tujuan belajar:** Pembaca bisa mengubah teks menjadi token lalu vektor, dan membandingkan kemiripan dua teks. Modul ini menjembatani ke modul 11 dan modul 14.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa unduhan.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Embedding dan tokenisasi.

## Issue

Modul ini: [#27](https://github.com/anwarminarso/a2n.Learn/issues/27).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 9: Dasar jaringan saraf dan PyTorch](../modul-09-pytorch/). Tensor dari modul 9 dipakai lagi: vektor di modul ini adalah tensor satu dimensi.

## Cerita pembuka

Dua kartu kata diletakkan di peta. "Kucing" dan "tikar" sering muncul bersama, jadi kartunya berdekatan. "Kapal" dan "laut" ada di sudut lain. Kalimat adalah rata-rata posisi kartu katanya. Dua kalimat yang berbagi kartu menunjuk ke arah yang mirip.

Modul ini berhenti di situ. Attention dan Transformer menyusul di modul 11. Menyimpan vektor untuk dicari lagi menyusul di modul 14. Sel terakhir notebook hanya menunjuk ke kedua modul itu, tanpa mengisi arti istilahnya.

## Teori

Tokenisasi di sini adalah kegiatan membuat token, bukan entri kamus yang lain. Kalimat latihan ditulis di repo. Tidak ada data asli perusahaan, termasuk yang sudah disamarkan.

### token

Gunting kalimat pada spasi, lalu tulis huruf kecil. "Kucing Duduk" menjadi `kucing` dan `duduk`. Nama teknisnya **token**: potongan teks yang dijadikan satu satuan. Di mode cepat, satu token adalah satu kata.

**Batas analogi:** gunting spasi tidak sama dengan tokenizer model sungguhan, yang bisa memotong di tengah kata. Tanda baca yang menempel pada kata menjadi token lain. Kartu kata belum punya makna sebelum ada vektornya.

### embedding

Setiap token yang belum pernah dilihat mendapat satu vektor acak berukuran 8. Undiannya memakai `SEED`, jadi peta yang sama muncul lagi. Vektor kalimat adalah rata-rata vektor tokennya. Nama teknisnya **embedding**: vektor angka yang mewakili satu token atau satu potongan teks. Di mode cepat modul ini, vektornya untuk token.

**Batas analogi:** jarak di peta bukan arti kamus. Peta acak ini tidak mengetahui makna. Dua kata bisa dekat di peta hanya karena undian. Merata-ratakan vektor token menjadi vektor kalimat tidak menjamin dua kalimat yang mirip katanya mirip maknanya.

### kemiripan vektor

Kosinus mengukur arah dua jarum, dari -1 sampai 1. Panjang jarum diabaikan. Nama teknisnya **kemiripan vektor**: skor kosinus dua vektor.

Pada keluaran notebook, pasangan kucing-tikar mendapat `skor_dekat` 0.904473. Pasangan dengan kapal-laut mendapat `skor_jauh` -0.255504. Selisihnya 1.159976, melewati ambang 0.3.

**Batas analogi:** kosinus mengabaikan panjang jarum. Dua kalimat bisa berbagi kata tetapi beda maksud, dan skornya tetap tinggi. Skor ini bukan peluang benar. Pada latihan, pasangan yang jauh masih bisa berskor positif, karena peta acak tidak menaruh semua kata yang berbeda di arah yang berlawanan. Yang dicek adalah selisihnya, bukan tanda minusnya.

## Coba sendiri dulu, baru kode

Mana yang lebih mirip dengan "kucing duduk di tikar": "kucing tidur di tikar", atau "kapal layar menyeberang laut"?

Jawab dulu. Lalu buka `notebook.ipynb` dari sel pertama.

## Kasus nyata

Tiga kalimat sintetis ditulis langsung di notebook. Tidak ada unduhan data. Bukan data asli perusahaan.

Mode cepat tidak memanggil model Hugging Face. Mode penuh, bila jaringan dinyalakan dengan `A2N_UNDUH=1`, memuat `sentence-transformers/all-MiniLM-L6-v2` pada revisi `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Pemuatnya ada di `muat.py`. Argumennya `revision=revisi`, `use_safetensors=True`, `trust_remote_code=False`, dan `allow_patterns` yang sama dengan bagian Aturan. Mode cepat tidak menyalakan unduhan itu.

Vektor mode penuh, bila diunduh, tetap perlu dirata-rata dari token. Berkas pooling di repo model tidak ikut diunduh, karena pola unduh hanya mengizinkan bobot safetensors, config, dan tokenizer. Mode cepat tidak bergantung pada berkas itu.

## Kesalahan yang paling sering terjadi

1. Huruf besar dibiarkan, jadi "Kucing" dan "kucing" menjadi dua token. Notebook menulis huruf kecil dulu.
2. Skor jauh yang masih positif dianggap gagal. Yang dicek adalah selisih dengan skor dekat, minimal 0.3.
3. Peta acak dianggap sudah tahu arti kata. Peta ini hanya undian yang dikunci SEED.
4. Mode penuh tidak dijalankan pada mode cepat, karena mode cepat tidak punya jaringan. Unduhan hanya bila `A2N_UNDUH=1`.
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

1. Apa beda token mode cepat dengan tokenizer model sungguhan?
2. Kosinus memakai panjang vektor, atau hanya arahnya?
3. Pada keluaran notebook, selisih skor melewati 0.3, atau tidak?

## Kunci jawaban

1. Mode cepat memotong pada spasi. Tokenizer model sungguhan bisa memotong di tengah kata.
2. Hanya arahnya. Panjang jarum diabaikan.
3. Melewati. `selisih_skor` 1.159976.

## Sumber

- Hugging Face. *Summary of the tokenizers*. <https://huggingface.co/docs/transformers/tokenizer_summary>
- NumPy developers. `numpy.linalg.norm`. <https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html>
- Reimers, Nils, and Iryna Gurevych. *Sentence-BERT*. <https://arxiv.org/abs/1908.10084>

## Istilah baru

Arti, perumpamaan, dan batas analogi ada di bagian Teori dan di [kamus](../../docs/kamus-istilah.md). Tiga istilah mengisi satu sesi.

### Sesi 1

1. token
2. embedding
3. kemiripan vektor

## Garis besar bagian

1. Cerita pembuka.
2. Teori tiga istilah.
3. Coba sendiri dulu, baru kode.
4. Tiga kalimat sintetis, plus catatan revisi untuk mode penuh.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi.

Sel terakhir notebook menunjuk ke modul 11 dan modul 14 tanpa mengisi arti istilah modul itu.

## Rencana latihan

- Tokenkan "Burung Biru Terbang".
- Bandingkan "mobil merah cepat" dengan "mobil biru cepat", lalu dengan "gunung tinggi bersalju".
- Selisih skor minimal 0.3. Peta latihannya diundi lagi, jadi angkanya tidak sama dengan pelajaran, dan ambangnya tetap.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Setiap sel siswa 16 baris atau lebih tidak dipakai.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Selisih skor kemiripan pasangan dekat dan pasangan jauh minimal 0.3.
- Mode cepat tidak mengunduh model. Bila mode penuh mengunduh, revisi yang dipin di register yang dipakai, dan lisensi sudah dicek sebelum unduh.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Beberapa kalimat sintetis, vektor kecil dari generator di notebook, jalan di CPU. Tidak ada unduhan.

### mode penuh

Opsional. `sentence-transformers/all-MiniLM-L6-v2` pada revisi yang dipin, di GPU MyLegion7i bila mesin itu memakainya. Hasil dinilai dari log mentah.

## Model dan dataset

- Dataset: kalimat sintetis yang ditulis di notebook.
- Mode penuh: `sentence-transformers/all-MiniLM-L6-v2`. Lisensi Apache-2.0. SHA `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, dicek 2026-11-13. Berkas `model.safetensors` ada. Repo itu juga memuat pickle `pytorch_model.bin`, dan pola unduh tidak memuatnya.
- Mode cepat tidak memakai model itu.
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
token ['kucing', 'duduk']
skor_dekat 0.904473
skor_jauh -0.255504
selisih_skor 1.159976
model sentence-transformers/all-MiniLM-L6-v2
revisi 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
unduh False
menuju modul 11 dan modul 14
token_latihan ['burung', 'biru', 'terbang']
skor_dekat_latihan 0.926162
skor_jauh_latihan 0.521745
```
