# Modul 13: Menjalankan model lokal dengan Ollama

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menggabungkan adapter ke model dasar, mengubah hasilnya menjadi GGUF, mengimpornya ke Ollama yang hanya mengikat 127.0.0.1, dan membandingkannya dengan kontrol tanpa LoRA yang melewati jalur konversi yang sama.

Materi mode cepat sudah bisa dijalankan di CPU, tanpa torch dan tanpa unduhan. Impor ke Ollama bukan gerbang PR.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Menjalankan model lokal dengan Ollama.

## Issue

Modul ini: [#30](https://github.com/anwarminarso/a2n.Learn/issues/30).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 12: Fine-tune dengan LoRA](../modul-12-lora/).

Adapter dilarang masuk repo. Mode cepat membuat ulang adapter LoRA kecil langsung di modul ini: delapan puluh langkah, data sintetis, di CPU, tanpa torch. Lalu adapter itu digabung dan dibanding dengan kontrol tanpa LoRA.

Cara memperoleh perkakas untuk jalur sungguhan, di luar gerbang:

- Grup torch, karena `convert_hf_to_gguf.py` pada commit ini mengimpor torch: `uv sync --frozen --group torch` dari root repo. Paket `transformers` hanya masuk lewat grup itu. Gerbang tidak memasang grup itu.
- llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`: `git clone https://github.com/ggml-org/llama.cpp` lalu `git checkout ca89968a23a13e571a6b802a9891d22763153b61`. Commit ini dicek 2026-11-12: ada `convert_hf_to_gguf.py` di akar dan paket gguf-py di folder `gguf-py`. Tidak disalin ke repo ini.
- gguf-py dipakai dari checkout itu untuk membaca metadata dan jumlah tensor berkas GGUF.
- Ollama 0.40.14 adalah versi referensi yang diuji untuk mode penuh. Berkas rilis ada di https://github.com/ollama/ollama/releases/tag/v0.40.14. Mesin gerbang PR tidak diasumsikan memasang Ollama.

## Cerita pembuka

Dapur rumah hanya membaca kartu dengan format tertentu. Resep yang sudah dicetak, plus stiker di pinggirnya, belum bisa masuk ke jendela dapur.

Kamu menyalin isi stiker ke dalam resep, lalu membuang stikernya. Itu penggabungan adapter. Lalu kamu menyalin lembar itu menjadi kartu yang dipahami dapur. Kartu itu GGUF. Kamu juga menyalin resep tanpa stiker, dengan cara yang sama, supaya rasanya bisa dibanding. Jendela dapur hanya membuka ke dalam rumah, yaitu `127.0.0.1`. Program yang menunggu di jendela itu peladen lokal. Nama alatnya Ollama.

## Teori

Mode cepat memakai vektor empat angka, bukan berkas model. Jumlah tensor yang dihitung adalah satu vektor sesudah digabung, dan satu vektor untuk kontrol. Keduanya sama banyak. Yang beda adalah angkanya.

### GGUF

Kartu resep untuk dapur rumah, bukan kertas asal dari percetakan. Nama teknisnya **GGUF**: format berkas yang menyimpan model yang sudah digabung, supaya peladen lokal bisa membacanya.

Konversi sungguhan memakai `convert_hf_to_gguf.py` pada commit yang dipin. Jangan memakai pilihan unduh jarak jauh pada skrip itu, karena unduhan model hanya lewat `muat.py` dengan revisi yang dipin. Berkas GGUF tidak masuk repo.

**Batas analogi:** kartu itu bukan adapter dan bukan safetensors. Mode cepat hanya menghitung jumlah tensor yang akan disalin. Mode cepat tidak menulis berkas GGUF.

### penggabungan adapter

Isi stiker disalin ke resep, lalu stikernya dibuang, supaya yang dibaca hanya satu lembar. Nama teknisnya **penggabungan adapter**: menambahkan perubahan LoRA ke bobot dasar sehingga hasilnya satu model utuh tanpa bagian terpisah.

Kontrol tanpa LoRA adalah resep yang tidak menerima isi stiker. Bentuknya tetap sama, jadi jalur konversi berikutnya sama.

**Batas analogi:** setelah digabung, stiker tidak bisa dilepas dari lembar itu. Jumlah tensor tetap sama. Yang berubah adalah angkanya. Pada keluaran notebook, `beda_skor` 4.504429, melewati ambang `0.5`.

### peladen lokal

Jendela dapur yang hanya membuka ke dalam rumah. Nama teknisnya **peladen lokal**: program di komputer sendiri yang melayani permintaan, baik model maupun RAG, dan hanya menerima sambungan dari `127.0.0.1`.

Di Linux dan macOS:

```bash
OLLAMA_HOST=127.0.0.1:11434 ollama serve
```

Di Windows, pada jendela perintah:

```bat
set OLLAMA_HOST=127.0.0.1:11434
ollama serve
```

Berkas `Modelfile` untuk model yang sudah digabung hanya menunjuk berkas lokal:

```text
FROM ./gabungan.gguf
```

Lalu `ollama create a2n-gabung -f Modelfile`. Ulangi dengan `kontrol.gguf` dan nama `a2n-kontrol`. Ajukan satu kalimat yang sama ke keduanya, lalu catat jawabannya. Impor ini bukan gerbang PR.

**Batas analogi:** alamat itu bukan janji jawaban benar. Mode cepat tidak menyalakan jendela itu. Mengikat alamat lain tidak diajarkan.

## Coba sendiri dulu, baru kode

Jawab dulu. Jangan gulir ke kunci.

Resep `[1.0, 2.0]` ditambah catatan `[0.5, 0.0]`. Berapa hasil gabungan, dan berapa kontrol yang tidak ditambah?

Setelah itu buka `notebook.ipynb` dan jalankan dari sel pertama.

## Kasus nyata

Angka sintetis dibuat ulang di notebook ini dengan `SEED`, bukan diambil dari berkas adapter modul 12. Bukan data asli perusahaan. Tidak ada unduhan.

Set uji sepuluh baris yang sama diukur sebelum dan sesudah adapter dibuat ulang. Lalu satu baris uji yang sama dipakai untuk membandingkan skor gabungan dan skor kontrol tanpa LoRA.

## Kesalahan yang paling sering terjadi

1. Mengambil berkas adapter dari repo. Mode cepat membuat ulang adapter LoRA kecil di memori.
2. Kontrol ikut menerima catatan LoRA. Kontrol adalah bobot dasar yang tidak ditambah.
3. Hanya model dengan LoRA yang dikonversi. Kontrol harus melewati `convert_hf_to_gguf.py` yang sama.
4. Ollama dibuka ke alamat selain `127.0.0.1`.
5. Berkas GGUF di-commit. Berkas itu tidak masuk repo.

## Cara menjalankan

Perintah gerbang, dari root repo:

```bash
uv sync --frozen
uv run pytest
```

Jalur GGUF sungguhan adalah sketsa opsional, belum diuji gerbang. Setelah gerbang lulus, dan hanya bila kamu memang ingin mencoba sketsa itu:

1. Dari root repo: `uv sync --frozen --group torch`. Paket `transformers` hanya masuk lewat grup torch.
2. Contoh singkat di bawah menggabungkan LoRA lalu memanggil `save_pretrained`, sehingga ada `folder-gabungan` dan `folder-kontrol`. Ini bukan latihan LoRA sungguhan: tidak ada putaran latih. Sketsa ini belum diuji gerbang. Dari root repo, dengan interpreter venv proyek:

```bash
A2N_UNDUH=1 uv run python - << 'PY'
import sys

sys.path.insert(0, "phase2-ai")
sys.path.insert(0, "phase2-ai/modul-13-model-lokal")
from muat import muat_dasar
from peft import LoraConfig, get_peft_model

tokenizer, dasar = muat_dasar()
dasar.save_pretrained("folder-kontrol")
tokenizer.save_pretrained("folder-kontrol")
konfig = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"], bias="none")
beradapter = get_peft_model(dasar, konfig)
gabungan = beradapter.merge_and_unload()
gabungan.save_pretrained("folder-gabungan")
tokenizer.save_pretrained("folder-gabungan")
PY
```

3. Checkout llama.cpp pada commit `ca89968a23a13e571a6b802a9891d22763153b61` ada di folder `llama.cpp/`. Jangan unduh model lewat pilihan jarak jauh pada skrip konversi. Perintah berikut dijalankan dari root repo dengan `uv run python`, bukan `python` polos:

```bash
uv run python llama.cpp/convert_hf_to_gguf.py folder-gabungan --outfile gabungan.gguf --outtype f16
uv run python llama.cpp/convert_hf_to_gguf.py folder-kontrol --outfile kontrol.gguf --outtype f16
PYTHONPATH=llama.cpp/gguf-py uv run python -c "from gguf import GGUFReader; r=GGUFReader('gabungan.gguf'); print(len(r.tensors))"
```

4. Bandingkan jumlah tensor gabungan dan kontrol. Lalu impor ke Ollama yang hanya mengikat `127.0.0.1`, dengan satu kalimat yang sama. Ini bukan gerbang PR. Seluruh jalur GGUF sungguhan ini sketsa opsional, belum diuji gerbang.

Sel pertama setiap notebook berisi `SEED = 42`. Tiap sel kode setelah sel pertama memuat satu ide.

## Cek pemahaman

1. Apa beda bobot gabungan dan kontrol tanpa LoRA?
2. Mengapa jumlah tensor keduanya sama?
3. Alamat dengar Ollama yang diajarkan di modul ini apa?

## Kunci jawaban

1. Kontrol adalah bobot dasar. Gabungan adalah bobot dasar ditambah catatan LoRA. Pada keluaran, `beda_skor` 4.504429.
2. Catatan sudah disalin ke dalam bobot, jadi yang tersisa satu vektor, sama seperti kontrol. `jumlah_sama ya`.
3. `127.0.0.1`.

## Sumber

- llama.cpp. `convert_hf_to_gguf.py` pada commit `ca89968a23a13e571a6b802a9891d22763153b61`. <https://github.com/ggml-org/llama.cpp/blob/ca89968a23a13e571a6b802a9891d22763153b61/convert_hf_to_gguf.py>
- ggml. *GGUF*. <https://github.com/ggml-org/ggml/blob/master/docs/gguf.md>
- Ollama. Rilis `v0.40.14`. <https://github.com/ollama/ollama/releases/tag/v0.40.14>

## Istilah baru

### Sesi 1

1. GGUF
2. penggabungan adapter
3. peladen lokal

## Garis besar bagian

1. Cerita pembuka sehari-hari.
2. Teori tiga istilah.
3. Coba sendiri dulu, baru kode.
4. Kasus angka sintetis, kontrol tanpa LoRA pada jalur yang sama.
5. Kesalahan yang paling sering terjadi.
6. Cek pemahaman dengan kunci jawaban.
7. Sumber resmi di bagian Sumber.

Notebook, latihan, dan kunci ada di folder ini. Mode cepat diuji tanpa jaringan, tanpa torch, dan tanpa Ollama.

## Rencana latihan

- Jumlahkan `[1.0, 2.0]` dengan `[0.5, 0.0]`, dan tulis juga vektor yang tidak ditambah.
- Cek bahwa beda skor gabungan dan kontrol minimal `0.5`.

## Kriteria lulus

Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.
- Mode cepat membuat ulang adapter LoRA kecil di CPU, bukan mengambil berkas adapter dari repo. Kerugian pada set uji turun minimal `0.15`. Bobot dasar tidak berubah.
- Model dengan LoRA dan kontrol tanpa LoRA sama-sama punya satu tensor pada mode cepat, dan sama-sama lewat `convert_hf_to_gguf.py` pada commit `ca89968a23a13e571a6b802a9891d22763153b61` bila jalur sungguhan dijalankan. gguf-py membaca metadata dan jumlah tensor. Berkas GGUF tidak masuk repo. Beda skor pada satu baris uji minimal `0.5`.
- Impor kedua berkas GGUF ke Ollama 0.40.14 di `127.0.0.1`, lalu bandingkan jawaban dengan kontrol, adalah mode penuh. Impor ini bukan gerbang PR.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus di CPU, tanpa torch dan tanpa jaringan. Buat ulang adapter LoRA kecil, gabungkan, bandingkan dengan kontrol tanpa LoRA, lalu catat jumlah tensor yang sama. Nama skrip `convert_hf_to_gguf.py` dan alamat `127.0.0.1` dicetak, tidak dijalankan. Ini gerbang tiap PR.

### mode penuh

Sketsa opsional, belum diuji gerbang. Konversi sungguhan ke GGUF pada commit llama.cpp `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor ke Ollama 0.40.14 yang hanya mengikat `127.0.0.1`, untuk model dengan LoRA dan untuk kontrol tanpa LoRA. GPU di MyLegion7i dipakai bila penggabungan model besar memerlukannya. Hasil dinilai dari log mentah. Bukan gerbang PR.

## Model dan dataset

- Dataset: angka sintetis yang dibuat ulang di notebook. Bukan data asli perusahaan.
- Model dasar: `HuggingFaceTB/SmolLM2-135M-Instruct`. Lisensi Apache-2.0. SHA `12fd25f77366fa6b3b4b768ec3050bf629380bac`, dicek 2026-11-13. Berkas `model.safetensors` ada. Repo ini juga berisi pickle `training_args.bin`.
- Mode penuh: `Qwen/Qwen2.5-0.5B-Instruct`. Lisensi Apache-2.0. SHA `7ae557604adf67be50417f59c2c2f167def9a775`.
- Kontrol: model dasar yang sama, tanpa adapter, lewat jalur GGUF yang sama.
- Skrip `convert_hf_to_gguf.py` dan gguf-py diambil dari llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61` saat jalur sungguhan dijalankan. Tidak disalin ke repo.
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
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul ini memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.

## Keluaran mode cepat

Angka di bawah disalin dari keluaran `notebook.ipynb` dan `latihan-kunci.ipynb`.

```
baris_latih 30
baris_uji 10
kerugian_uji_sebelum 0.246913
kerugian_uji_sesudah 0.050404
selisih_uji 0.196509
bobot_tetap ya
tensor_gabung 1
tensor_kontrol 1
jumlah_sama ya
skor_gabung -4.496645
skor_kontrol 0.007784
beda_skor 4.504429
skrip convert_hf_to_gguf.py
commit ca89968
alamat 127.0.0.1
impor_ollama bukan_gerbang
model HuggingFaceTB/SmolLM2-135M-Instruct
revisi 12fd25f77366fa6b3b4b768ec3050bf629380bac
model_penuh Qwen/Qwen2.5-0.5B-Instruct
revisi_penuh 7ae557604adf67be50417f59c2c2f167def9a775
unduh False
gabung_latihan [1.5, 2.0]
kontrol_latihan [1.0, 2.0]
```
