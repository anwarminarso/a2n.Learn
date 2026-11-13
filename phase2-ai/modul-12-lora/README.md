# Modul 12: Fine-tune dengan LoRA

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa melakukan penyetelan halus (fine-tune) pada model kecil dengan LoRA, lalu mengukur sebelum dan sesudah pada set uji yang sama.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa torch dan tanpa unduhan.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Fine-tune dengan LoRA.

## Issue

Modul ini: [#29](https://github.com/anwarminarso/a2n.Learn/issues/29).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 11: Transformer](../modul-11-attention-transformer/).

Mode cepat hanya memakai numpy. Jalur LoRA nyata memakai grup opsional torch, CPU saja. Pasang dari root repo, folder yang berisi `pyproject.toml`:

```bash
uv sync --group torch
```

Lalu set `A2N_TORCH=1` sebelum menjalankan notebook. `uv sync` biasa tidak memasang grup itu. Gerbang PR tidak memasangnya.

Roda CPU Python 3.14 untuk torch ada di Linux, Windows, dan macOS Apple Silicon. macOS Intel tidak didukung, karena tidak ada roda cp314 di indeks CPU.

## Cerita pembuka

Buku resep sudah dicetak. Kamu tidak mencetak ulang seluruh buku hanya karena supnya kurang garam. Kamu menempel catatan kecil di pinggir halaman: "tambah sedikit garam".

Catatan itu LoRA. Melatih catatan pada beberapa contoh masakan adalah penyetelan halus (fine-tune). Buku resepnya, yaitu bobot dasar, tidak berubah. Catatan itu disebut adapter. Adapter tidak disimpan ke repo dan tidak diunggah.

## Teori

Data di mode cepat empat angka sintetis per baris, dibuat di notebook dengan `SEED`. Bukan data asli perusahaan. Labelnya 0 atau 1. Fungsi kerugian tetap rata-rata selisih yang dikuadratkan, seperti modul 3.

### penyetelan halus (fine-tune)

Adonan sudah diulen orang lain. Kamu hanya menambah bumbu untuk hidangan hari ini, bukan mengaduk tepung dari nol. Nama teknisnya **penyetelan halus (fine-tune)**: melatih lagi model yang sudah ada pada data tugas kita.

Di mode cepat, model yang sudah ada adalah satu vektor bobot yang dibekukan. Yang dilatih hanya catatan kecil, delapan puluh langkah.

**Batas analogi:** delapan puluh langkah pada model mini bukan latihan model obrolan sampai selesai. Menyetel pada data latih tidak menilai data uji. Ini bukan menyesuaikan keluaran dengan nilai manusia. Topik itu belum menjadi entri kamus.

### LoRA

Catatan kecil hanya punya satu arah. Perubahan bobot adalah skalar kali vektor, jadi pangkatnya satu. Nama teknisnya **LoRA**: cara penyetelan halus yang hanya melatih dua kumpulan angka kecil. Perubahan bobot adalah hasil kali keduanya, dan pangkatnya rendah.

Pada latihan tangan, vektor `[1.0, 0.0]` dikali `0.5` menjadi `[0.5, 0.0]`.

**Batas analogi:** catatan kecil hanya menggeser resep pada arah yang pangkatnya rendah. Perubahan yang butuh banyak arah bebas tidak muat. Di mode cepat catatan itu satu vektor dan satu skalar, bukan model obrolan utuh.

### adapter

Stiker resep bisa dilepas. Buku resep tetap di rak. Nama teknisnya **adapter**: kumpulan angka kecil hasil LoRA yang bisa dipasang pada model dasar. Bobot dasar tidak ikut disimpan di dalamnya.

Notebook mencetak `adapter_disimpan tidak`. Tidak ada berkas yang ditulis.

**Batas analogi:** stiker tidak bisa dipakai tanpa buku resep yang sama. Modul ini tidak menyimpan stiker ke repo dan tidak mengunggahnya. Menyalin isi stiker ke dalam buku adalah penggabungan adapter, dan itu modul 13.

## Coba sendiri dulu, baru kode

Jawab dulu. Jangan gulir ke kunci.

Vektor `[1.0, 0.0]` dikali `0.5`. Hasilnya apa?

Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

Empat puluh baris angka dibuat dengan `np.random.default_rng(SEED)`. Bukan unduhan. Bukan data asli perusahaan.

Tiga puluh baris untuk belajar, sepuluh baris untuk uji. Set uji yang sama dipakai sebelum dan sesudah. Bobot dasar `W` disalin dulu, lalu dicek tetap sama. Yang bergerak hanya `a` dan `b`.

Ambang mode cepat: selisih kerugian pada set uji minimal `0.15`, dan jumlah salah pada set uji turun.

## Kesalahan yang paling sering terjadi

1. Seluruh bobot ikut dilatih. Di mode cepat hanya catatan kecil yang digeser.
2. Skor sebelum dan sesudah diukur pada baris yang berbeda. Notebook memakai set uji yang sama.
3. Adapter disimpan ke repo atau diunggah. Notebook tidak menulis berkas.
4. Gerbang diminta mengunduh model. Mode cepat mencetak `unduh False`.
5. Angka di laporan ditulis dari ingatan. Salin dari keluaran notebook.

## Cara menjalankan

Perintah dijalankan dari root repo, folder yang berisi `pyproject.toml` dan `uv.lock`:

```bash
uv sync --frozen
uv run pytest
```

Jalur LoRA nyata, CPU saja:

```bash
uv sync --group torch
```

Lalu `A2N_TORCH=1`. Tanpa itu, sel peft mencetak kalimat lewati. Unduhan model hanya bila `A2N_UNDUH=1`, lewat `muat_smol()` di `muat.py`. Mode cepat tidak memanggil fungsi itu.

Sel pertama setiap notebook berisi `SEED = 42`. Tiap sel kode setelah sel pertama memuat satu ide.

## Cek pemahaman

1. Apa yang dibekukan, dan apa yang dilatih?
2. Pada keluaran notebook, selisih kerugian uji melewati `0.15`, atau tidak?
3. Adapter dari latihan ini disimpan ke mana?

## Kunci jawaban

1. Bobot dasar dibekukan. Yang dilatih adalah catatan kecil, yaitu vektor `a` dan skalar `b`.
2. Melewati. `selisih_uji` 0.196509.
3. Tidak ke mana-mana. `adapter_disimpan tidak`. Tidak masuk repo dan tidak diunggah.

## Sumber

- Hu, Edward J., dkk. *LoRA: Low-Rank Adaptation of Large Language Models*. <https://arxiv.org/abs/2106.09685>
- Hugging Face. *PEFT*. <https://huggingface.co/docs/peft>
- PyTorch contributors. `torch.nn.Linear`. <https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html>

## Istilah baru yang direncanakan

Arti, perumpamaan, dan batas analogi ada di bagian Teori dan di [kamus](../../docs/kamus-istilah.md). Nama di bawah tetap paling banyak tiga per sesi. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. penyetelan halus (fine-tune)
2. LoRA
3. adapter

## Garis besar bagian

1. Cerita pembuka sehari-hari.
2. Teori tiga istilah.
3. Coba sendiri dulu, baru kode.
4. Kasus pada angka sintetis, set uji yang sama.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi di bagian Sumber.

Notebook, latihan, dan kunci ada di folder ini. Mode cepat diuji tanpa jaringan dan tanpa torch.

## Rencana latihan

- Hitung `0.5` kali `[1.0, 0.0]` sebelum membuka kunci.
- Cek bahwa selisih kerugian pada set uji yang sama minimal `0.15`.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Pada set uji yang sama, kerugian sesudah lebih kecil, selisih minimal `0.15`. Jumlah salah pada set uji juga turun.
- Bobot dasar tidak berubah. Adapter tidak masuk repo dan tidak di-push ke Hugging Face.
- Jalur peft hanya berjalan bila `A2N_TORCH=1`. Mode cepat tidak memanggil torch.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Model sangat kecil, 80 langkah, jalan di CPU, tanpa torch dan tanpa unduhan. Ini gerbang tiap PR. Data angka sintetis dari generator di notebook.

### mode penuh

Opsional. `Qwen/Qwen2.5-0.5B-Instruct` pada revisi yang dipin, di GPU MyLegion7i bila mesin itu memakainya. Hasil dinilai dari log mentah. Bukan gerbang PR. Unduhan hanya lewat `muat.py` bila `A2N_UNDUH=1`.

## Model dan dataset kandidat

- Dataset mode cepat: empat puluh baris angka sintetis di notebook. Bukan data asli perusahaan.
- Model mode cepat untuk unduhan opsional: `HuggingFaceTB/SmolLM2-135M-Instruct`. Lisensi Apache-2.0. SHA `12fd25f77366fa6b3b4b768ec3050bf629380bac`, dicek 2026-11-13. Berkas `model.safetensors` ada. Repo ini juga berisi pickle `training_args.bin`. Pola unduh tidak memuatnya.
- Mode penuh: `Qwen/Qwen2.5-0.5B-Instruct`. Lisensi Apache-2.0. SHA `7ae557604adf67be50417f59c2c2f167def9a775`. Pada revisi ini tidak ada `pytorch_model.bin` dan tidak ada `training_args.bin`.
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

Angka di bawah disalin dari keluaran `notebook.ipynb` dan `latihan-kunci.ipynb`. Baris `jalur_lora nyala` dan baris peft hanya muncul bila `A2N_TORCH=1`. Baris lewati muncul bila jalur itu mati.

```
baris_latih 30
baris_uji 10
pangkat 1
kerugian_uji_sebelum 0.246913
salah_sebelum 4
kerugian_uji_sesudah 0.050404
selisih_uji 0.196509
salah_sesudah 1
bobot_tetap ya
adapter_disimpan tidak
model HuggingFaceTB/SmolLM2-135M-Instruct
revisi 12fd25f77366fa6b3b4b768ec3050bf629380bac
model_penuh Qwen/Qwen2.5-0.5B-Instruct
revisi_penuh 7ae557604adf67be50417f59c2c2f167def9a775
unduh False
jalur_lora lewati
jalur_lora nyala
lewati_beku Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_peft Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_latih_peft Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
lewati_hasil_peft Jalur ini dilewati. Pasang grup dengan uv sync --group torch, lalu set A2N_TORCH=1.
beku siap
adapter_peft ya
turun_peft ya
delta_latihan [0.5, 0.0]
```
