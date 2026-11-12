# Register lisensi model

Tempat mencatat kandidat model Fase 2 sebelum ada unduhan bobot. Materi belum memilih revisi, jadi setiap baris berstatus **belum dipin**.

Lisensi di kolom ini dibaca dari kartu model Hugging Face pada 2026-11-12, lewat metadata kartu, tanpa mengunduh bobot. Saat sebuah revisi dipin, lisensi dicek lagi pada revisi itu, sebelum unduh. Unduhan hanya boleh untuk model kecil berlisensi Apache-2.0 atau MIT, format safetensors, dengan `trust_remote_code=False`.

Tidak ada kandidat di tabel yang lisensinya di luar Apache-2.0 atau MIT. Kandidat baru yang lisensinya lain tidak diunduh. Tandai di kolom catatan, dan jangan tambahkan bobotnya ke repo.

Modul 9 tidak mengunduh model. Jaringannya ditulis di materi.

| Kandidat | Modul | Lisensi | Status | Catatan |
|---|---|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | 10, 14 | Apache-2.0 | belum dipin | Kartu model. Dipakai bila mode penuh butuh embedding. |
| `prajjwal1/bert-tiny` | 11 | MIT | belum dipin | Kartu model bertanda MIT. Kandidat mode cepat untuk klasifikasi teks. |
| `distilbert/distilbert-base-uncased` | 11 | Apache-2.0 | belum dipin | Id kanonik. Kartu model Apache-2.0. Kandidat mode penuh, opsional. |
| `HuggingFaceTB/SmolLM2-135M-Instruct` | 12, 13, 15 | Apache-2.0 | belum dipin | Kartu model. Kandidat mode cepat untuk LoRA, jalur GGUF, dan agen bila perlu model. |
| `Qwen/Qwen2.5-0.5B-Instruct` | 12, 13 | Apache-2.0 | belum dipin | Kartu model. Kandidat mode penuh yang opsional di MyLegion7i. |

Adapter, indeks vektor, dan berkas GGUF tidak masuk repo dan tidak di-push ke Hugging Face. Ollama hanya mengikat 127.0.0.1.
