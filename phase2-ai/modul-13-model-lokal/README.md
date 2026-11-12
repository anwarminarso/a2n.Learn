# Modul 13: Menjalankan model lokal

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menggabungkan adapter ke model dasar, mengubah hasilnya menjadi GGUF, mengimpornya ke Ollama yang hanya mengikat 127.0.0.1, dan membandingkannya dengan kontrol tanpa LoRA yang melewati jalur konversi yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 12: Penyelarasan dengan LoRA](../modul-12-lora/).

## Mengapa modul ini

Tidak dipecah. GGUF, penggabungan adapter, dan peladen lokal adalah tiga istilah. Kontrol tanpa LoRA memakai jalur konversi yang sama, jadi bukan sesi baru. Ollama adalah nama alat untuk peladen lokal, belum menjadi entri kamus. Bila uji jalan menunjukkan konversi tidak muat satu sesi duduk, pemecahan ditinjau lagi.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. GGUF
2. penggabungan adapter
3. peladen lokal

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

- Gabungkan adapter ke model dasar.
- Ubah hasil gabungan menjadi GGUF dengan skrip llama.cpp `convert_hf_to_gguf.py`.
- Impor GGUF ke Ollama yang mengikat hanya ke 127.0.0.1.
- Ulangi jalur yang sama untuk kontrol tanpa LoRA.
- Bandingkan keduanya dengan ambang, bukan teks jawaban yang persis.
- Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF wajib.

## Rencana latihan

- Pakai satu prompt yang sama untuk model dengan LoRA dan untuk kontrol tanpa LoRA.
- Catat bahwa impor safetensors langsung tidak dipakai.
- Periksa alamat dengar Ollama adalah 127.0.0.1.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Model dengan LoRA dan kontrol tanpa LoRA sama-sama lewat `convert_hf_to_gguf.py`, lalu impor GGUF.
- Ollama hanya mengikat 127.0.0.1.
- Perbedaan jawaban diukur dengan ambang. Ambang belum dipilih.

## Mode cepat dan mode penuh

### mode cepat

Model sangat kecil, beberapa langkah konversi, jalan di CPU.

### mode penuh

Kandidat modul 12, pada GPU bila penggabungan memerlukannya. Referensi perangkat: laptop RTX 5070 8 GB VRAM. Ollama tetap di mesin lokal.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Model dasar: kandidat modul 12, belum dipin.
- Kontrol: model dasar yang sama, tanpa adapter, lewat jalur GGUF yang sama.
- Skrip: `convert_hf_to_gguf.py` dari llama.cpp. Skrip itu tidak disalin ke repo pada langkah placeholder ini.
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
