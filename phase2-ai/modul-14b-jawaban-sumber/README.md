# Modul 14b: Jawaban dengan sumber

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menyusun jawaban yang menyebut sumber potongan, dan menilai jawaban mengarang dengan ambang sederhana.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 14a: Potongan teks dan penyimpan vektor](../modul-14a-penyimpan-vektor/).

## Mengapa modul ini

Menjawab dengan sumber dan menilai jawaban mengarang adalah sesi duduk lain. Tiga istilah: RAG, jawaban mengarang, dan kutipan sumber.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. RAG
2. jawaban mengarang
3. kutipan sumber

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

- Susun jawaban yang menyebut kutipan sumber dari potongan yang diambil.
- Siapkan soal yang jawabannya tidak ada di dokumen.
- Nilai jawaban mengarang dengan ambang, bukan dengan kalimat yang persis.

## Rencana latihan

- Satu soal yang sumbernya ada di potongan.
- Satu soal jebakan yang sumbernya tidak ada.
- Jawaban jebakan harus menolak atau ditandai sebagai jawaban mengarang.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Soal yang bersumber menyebut potongan yang diambil. Bentuk kutipan ditulis saat materi diisi.
- Soal jebakan tidak dinilai dengan kalimat persis. Lulus bila ada penolakan atau tanda jawaban mengarang, dengan ambang hitungan yang belum dipilih.

## Mode cepat dan mode penuh

### mode cepat

Dokumen sintetis kecil, jalan di CPU.

### mode penuh

Kandidat model kecil untuk menyusun jawaban, pada GPU. Referensi perangkat: laptop RTX 5070 8 GB VRAM.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Dokumen dan penyimpan mengikuti modul 14a.
- Model jawaban, bila dipakai: kandidat kecil modul 12, belum dipin.
- Jawaban boleh disusun dari potongan saja, tanpa model generatif. Pilihan itu ditunda ke materi.
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
