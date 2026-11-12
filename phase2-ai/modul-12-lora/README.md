# Modul 12: Fine-tune dengan LoRA

**Status:** PLACEHOLDER

**Tingkat:** pro

**Tujuan belajar:** Pembaca bisa melakukan penyetelan halus (fine-tune) pada model kecil dengan LoRA pada dataset instruksi kecil, lalu mengukur sebelum dan sesudah pada set uji yang sama.

Isi materi belum ditulis. Halaman ini adalah rencana, bukan bahan ajar.

Nama pada [docs/ROADMAP.md](../../docs/ROADMAP.md): Fine-tune dengan LoRA.

## Issue

Modul ini: [#29](https://github.com/anwarminarso/a2n.Learn/issues/29).

Tracking Fase 2: [#33](https://github.com/anwarminarso/a2n.Learn/issues/33).

## Prasyarat

Modul sebelumnya: [Modul 11: Transformer](../modul-11-attention-transformer/).

## Mengapa modul ini

Modul ini utuh, satu sesi. Penyetelan halus (fine-tune), LoRA, dan adapter adalah tiga istilah. Penyetelan halus (fine-tune) adalah satu entri: melatih lagi model yang sudah ada pada data instruksi kecil. Alignment, yaitu menyesuaikan keluaran model dengan nilai manusia, adalah topik lain dan belum menjadi entri kamus. Mengukur sebelum dan sesudah memakai set uji yang sama, bukan modul terpisah.

## Istilah baru yang direncanakan

Paling banyak tiga istilah baru pada tiap sesi. Arti, perumpamaan, dan batas analogi belum ditulis. Baris kamus berstatus PLACEHOLDER. Modul ini tidak dipecah menjadi folder berhuruf.

### Sesi 1

1. penyetelan halus (fine-tune)
2. LoRA
3. adapter

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

- Siapkan dataset instruksi kecil, sintetis atau publik berlisensi jelas.
- Ukur model sebelum diubah, pasang LoRA untuk beberapa langkah, lalu ukur lagi pada set uji yang sama.
- Adapter tidak di-commit dan tidak di-push ke Hugging Face.

## Rencana latihan

- Kunci satu set uji, dipakai sebelum dan sesudah.
- Catat selisih skor. Ambang X belum dipilih.

## Kriteria lulus

Status bagian ini: DRAF. Angka ambang belum dipilih. Pengecekan memakai ambang, bukan angka persis.

- Merge diblok bila ada sel siswa 16 baris atau lebih.
- Mode cepat wajib lulus di CPU. Mode penuh GPU di MyLegion7i opsional dan dinilai dari log mentah.

- Skor sesudah lebih baik daripada skor sebelum, selisih minimal X, pada set uji yang sama. X belum dipilih.
- Adapter dari latihan ini tidak masuk repo dan tidak di-push ke Hugging Face.

## Mode cepat dan mode penuh

### mode cepat

Wajib lulus. Model sangat kecil, beberapa langkah, jalan di CPU.

### mode penuh

Opsional. Kandidat yang lebih besar pada GPU di MyLegion7i. Kecocokan memori diverifikasi dari log mentah, bukan di placeholder ini.

## Model dan dataset kandidat

Semua id di bawah kandidat, bukan pilihan final. Revisi belum dipilih. Lisensi pada tabel register dibaca dari kartu model, sebelum unduhan bobot, dan dicek lagi pada revisi yang dipin sebelum unduh.

- Kandidat mode cepat: `HuggingFaceTB/SmolLM2-135M-Instruct`. Lisensi kartu model Apache-2.0.
- Kandidat mode penuh: `Qwen/Qwen2.5-0.5B-Instruct`. Lisensi kartu model Apache-2.0.
- Dataset mode cepat: instruksi sintetis dari generator di repo.
- Status pin: belum dipin.

## Aturan

Bagian ini adalah gate placeholder. Aturan yang sama berlaku saat materi ditulis.

- Data hanya sintetis atau dataset publik. Data asli perusahaan dilarang sama sekali, termasuk yang sudah disamarkan.
- Tidak ada adapter atau indeks yang masuk repo atau di-push ke Hugging Face. Tidak ada file GGUF di repo.
- Mode cepat wajib lulus di CPU dan menjadi gerbang tiap PR. Mode penuh GPU di MyLegion7i opsional, dan dinilai dari log mentah.
- Unduhan hanya model kecil berlisensi Apache-2.0 atau MIT. Lisensi dicek sebelum unduh. Revisi Hugging Face di-pin. Hanya format safetensors. `trust_remote_code=False`. Kandidat dan lisensinya ada di [register lisensi model](../../docs/lisensi-model.md). Status pin: belum dipin.
- Setiap model Hugging Face di Fase 2 dimuat dengan `use_safetensors=True`.
- Pengecekan pakai ambang, misalnya loss turun minimal X, bukan angka persis.
- Ollama mengikat hanya ke 127.0.0.1. Versi referensi yang diuji: 0.40.14. Modul 13 memakai jalur GGUF: merge LoRA, lalu `convert_hf_to_gguf.py` pada llama.cpp commit `ca89968a23a13e571a6b802a9891d22763153b61`, lalu impor GGUF ke Ollama, dibanding kontrol lewat jalur yang sama.
- Modul 15: tools hanya allowlist read-only di folder sandbox, tanpa shell bebas, tanpa akses jaringan internal.
