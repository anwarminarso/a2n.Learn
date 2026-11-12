# Modul 12: Penyelarasan dengan LoRA

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa menyelaraskan model kecil dengan LoRA pada dataset instruksi kecil, lalu mengukur sebelum dan sesudah pada set uji yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

## Prasyarat

Modul sebelumnya: [Modul 11b: Klasifikasi teks dengan model siap pakai](../modul-11b-klasifikasi-teks/).

## Mengapa modul ini

Tidak dipecah. Penyelarasan, LoRA, dan adapter adalah tiga istilah. Pada breakdown tim, modul ini adalah fine-tune dengan LoRA. Fine-tune adalah sebutan bahasa Inggris untuk penyelarasan, bukan entri kamus kedua. Mode cepat membatasi jumlah langkah supaya tetap satu sesi duduk. Mengukur sebelum dan sesudah adalah satu latihan pada set uji yang sama, bukan modul terpisah.

## Istilah baru yang direncanakan

Paling banyak tiga. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus untuk nama di bawah berstatus PLACEHOLDER.

1. penyelarasan
2. LoRA
3. adapter

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

- Siapkan dataset instruksi kecil, publik berlisensi jelas atau sintetis dari generator di repo.
- Ukur model sebelum diubah, pada set uji.
- Pasang LoRA dan jalankan beberapa langkah pada mode cepat.
- Ukur lagi pada set uji yang sama.
- Adapter tidak di-commit dan tidak di-push ke Hugging Face bila datanya non-publik.

## Rencana latihan

- Kunci satu set uji, dipakai sebelum dan sesudah.
- Catat selisih skor. Ambang X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Skor sesudah lebih baik daripada skor sebelum, selisih minimal X, pada set uji yang sama. X belum dipilih.
- Adapter dan dataset dari data non-publik tidak masuk repo dan tidak di-push ke Hugging Face.

## Mode cepat dan mode penuh

### mode cepat

Model sangat kecil, beberapa langkah, jalan di CPU.

### mode penuh

Kandidat yang lebih besar, pada GPU. Referensi perangkat: laptop RTX 5070 8 GB VRAM. Kecocokan memori diverifikasi saat materi ditulis, bukan di placeholder ini.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih.

- Kandidat mode cepat: `HuggingFaceTB/SmolLM2-135M-Instruct`.
- Kandidat mode penuh: `Qwen/Qwen2.5-0.5B-Instruct`.
- Dataset mode cepat: instruksi sintetis dari generator di repo. Nama dataset publik belum dipilih.
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
