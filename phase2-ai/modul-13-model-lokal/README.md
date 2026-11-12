# Modul 13: Menjalankan model lokal dengan Ollama

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menggabungkan adapter ke model dasar, mengubah hasilnya menjadi GGUF, mengimpornya ke Ollama yang hanya mengikat 127.0.0.1, dan membandingkannya dengan kontrol tanpa LoRA yang melewati jalur konversi yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Menjalankan model lokal dengan Ollama.

## Issue

Modul ini: [#30](https://github.com/anwarminarso/a2n.Learn/issues/30).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 12: Fine-tune dengan LoRA](../modul-12-lora/).

Adapter dilarang masuk repo. Mode cepat membuat ulang adapter LoRA kecil langsung di modul ini: beberapa langkah, data sintetis, di CPU. Lalu adapter itu digabung, dikonversi ke GGUF, dan dicek.

Cara memperoleh perkakas:

- llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`: `git clone https://github.com/ggml-org/llama.cpp` lalu `git checkout ca89968a23a13e571a6b802a9891d22763153b61`. Commit ini dicek 2026-11-12: ada `convert_hf_to_gguf.py` di akar dan paket gguf-py di folder `gguf-py`. Tidak disalin ke repo ini.
- gguf-py dipakai dari checkout itu untuk membaca metadata dan jumlah tensor berkas GGUF.
- Ollama 0.40.14 adalah versi referensi yang diuji untuk mode penuh. Berkas rilis ada di https://github.com/ollama/ollama/releases/tag/v0.40.14. Mesin gerbang PR tidak diasumsikan memasang Ollama.

## Mengapa modul ini

Modul ini utuh, satu sesi. GGUF, penggabungan adapter, dan peladen lokal adalah tiga istilah. Kontrol tanpa LoRA memakai jalur konversi yang sama, jadi bukan modul baru. Ollama adalah nama alat untuk peladen lokal, belum menjadi entri kamus.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. GGUF
2. penggabungan adapter
3. peladen lokal

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

- Mode cepat membuat ulang adapter LoRA kecil di modul ini (beberapa langkah, CPU), menggabungkannya ke model dasar, lalu mengubah hasilnya menjadi GGUF dengan `convert_hf_to_gguf.py` pada commit `ca89968a23a13e571a6b802a9891d22763153b61`.
- Cek berkas GGUF dengan gguf-py dari checkout yang sama: metadata terbaca dan jumlah tensor dicatat. Ambang jumlah tensor belum dipilih.
- Ulangi jalur konversi yang sama untuk kontrol tanpa LoRA.
- Impor GGUF ke Ollama 0.40.14 yang mengikat hanya ke 127.0.0.1, lalu bandingkan dengan kontrol, adalah mode penuh. Mesin gerbang tidak diasumsikan memasang Ollama.

## Rencana latihan

- Pakai satu prompt yang sama untuk model dengan LoRA dan untuk kontrol tanpa LoRA.
- Periksa alamat dengar Ollama adalah 127.0.0.1. Pemeriksaan ini bagian mode penuh.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Mode cepat membuat ulang adapter LoRA kecil di CPU, bukan mengambil berkas adapter dari repo. Model dengan LoRA dan kontrol tanpa LoRA sama-sama lewat `convert_hf_to_gguf.py` pada commit `ca89968a23a13e571a6b802a9891d22763153b61`. gguf-py membaca metadata dan jumlah tensor. Berkas GGUF tidak masuk repo.
- Impor kedua berkas GGUF ke Ollama 0.40.14 di 127.0.0.1, lalu bandingkan jawaban dengan kontrol, adalah mode penuh. Impor ini bukan gerbang PR. Ambang belum dipilih.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus di CPU. Buat ulang adapter LoRA kecil (beberapa langkah), gabungkan, konversi ke GGUF pada commit llama.cpp `ca89968a23a13e571a6b802a9891d22763153b61`, lalu cek metadata dan jumlah tensor dengan gguf-py. Impor ke Ollama bukan bagian mode cepat.

### mode penuh

Opsional. Impor GGUF ke Ollama 0.40.14 yang hanya mengikat 127.0.0.1, untuk model dengan LoRA dan untuk kontrol tanpa LoRA, lalu bandingkan jawabannya. GPU di MyLegion7i dipakai bila penggabungan memerlukannya. Hasil dinilai dari log mentah.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Model dasar: kandidat modul 12, belum dipin. Lisensi mengikuti register.
- Kontrol: model dasar yang sama, tanpa adapter, lewat jalur GGUF yang sama.
- Skrip `convert_hf_to_gguf.py` dan gguf-py diambil dari llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61` saat gerbang dijalankan. Tidak disalin ke repo.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Setiap model Hugging Face dimuat dengan `use_safetensors=True` dan `trust_remote_code=False`.
- Unduhan dibatasi lewat `allow_patterns` hanya ke `*.safetensors`, `config.json`, `generation_config.json`, dan berkas tokenizer (`tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `vocab.txt`, `merges.txt`, `vocab.json`). Beberapa repo yang dipakai juga berisi berkas pickle seperti `pytorch_model.bin` atau `training_args.bin`.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul ini memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
