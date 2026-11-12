# Modul 13: Model lokal lewat Ollama

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menggabungkan adapter ke model dasar, mengubah hasilnya menjadi GGUF, mengimpornya ke Ollama yang hanya mengikat 127.0.0.1, dan membandingkannya dengan kontrol tanpa LoRA yang melewati jalur konversi yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Menjalankan model lokal dengan Ollama.

## Issue

Modul ini: [#30](https://github.com/anwarminarso/a2n.Learn/issues/30).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 12: Fine-tune LoRA pada model kecil](../modul-12-lora/).

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

- Gabungkan LoRA ke model dasar.
- Ubah hasil gabungan menjadi GGUF dengan skrip llama.cpp `convert_hf_to_gguf.py`.
- Impor GGUF ke Ollama yang mengikat hanya ke 127.0.0.1.
- Ulangi jalur yang sama untuk kontrol tanpa LoRA, lalu bandingkan dengan ambang.
- Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF wajib.

## Rencana latihan

- Pakai satu prompt yang sama untuk model dengan LoRA dan untuk kontrol tanpa LoRA.
- Periksa alamat dengar Ollama adalah 127.0.0.1.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Model dengan LoRA dan kontrol tanpa LoRA sama-sama lewat `convert_hf_to_gguf.py`, lalu impor GGUF.
- Ollama hanya mengikat 127.0.0.1.
- Perbedaan jawaban diukur dengan ambang. Ambang belum dipilih. Berkas GGUF tidak masuk repo.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Model sangat kecil, beberapa langkah konversi, jalan di CPU.

### mode penuh

Opsional. Kandidat modul 12 pada GPU di MyLegion7i bila penggabungan memerlukannya. Hasil dinilai dari log mentah. Ollama tetap di mesin lokal.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Model dasar: kandidat modul 12, belum dipin. Lisensi mengikuti register.
- Kontrol: model dasar yang sama, tanpa adapter, lewat jalur GGUF yang sama.
- Skrip `convert_hf_to_gguf.py` dari llama.cpp tidak disalin ke repo pada langkah placeholder ini.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Ollama Windows 0.40.14 tidak bisa mengimpor safetensors langsung karena butuh runtime MLX, jadi jalur GGUF lewat skrip llama.cpp `convert_hf_to_gguf.py` wajib.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
