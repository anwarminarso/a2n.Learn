# Register lisensi model

Tempat mencatat kandidat model Fase 2 sebelum ada unduhan bobot. Materi belum memilih revisi, jadi setiap baris berstatus **belum dipin**.

Lisensi dan format dibaca pada 2026-11-12 dari `https://huggingface.co/api/models/<id>`, tanpa mengunduh bobot. Kolom lisensi berasal dari `cardData.license`. Kolom format berasal dari `siblings` yang namanya berakhiran `.safetensors`. Saat sebuah revisi dipin, lisensi dan adanya berkas safetensors dicek lagi pada revisi itu, sebelum unduh. Unduhan hanya boleh untuk model kecil berlisensi Apache-2.0 atau MIT yang punya berkas `.safetensors`, dengan `trust_remote_code=False`.

`prajjwal1/bert-tiny` ditolak untuk mode cepat modul 11. `cardData.license` bertanda MIT. `siblings` berisi `pytorch_model.bin` dan tidak berisi berkas `.safetensors`. Id itu tidak masuk tabel unduhan.

Tidak ada kandidat di tabel yang lisensinya di luar Apache-2.0 atau MIT, dan tidak ada baris tanpa berkas safetensors. Kandidat baru yang lisensinya lain, atau yang tidak punya `.safetensors`, tidak diunduh.

Modul 9 tidak mengunduh model. Jaringannya ditulis di materi.

| Kandidat | Modul | Lisensi | Format | Status | Catatan |
|---|---|---|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | 10, 14 | Apache-2.0 | model.safetensors | belum dipin | cardData.license apache-2.0. siblings berisi model.safetensors. Dipakai bila mode penuh butuh embedding. |
| `google/bert_uncased_L-2_H-128_A-2` | 11 | Apache-2.0 | model.safetensors | belum dipin | cardData.license apache-2.0. siblings berisi model.safetensors. Kandidat mode cepat klasifikasi teks. Dua lapisan, hidden 128. |
| `distilbert/distilbert-base-uncased` | 11 | Apache-2.0 | model.safetensors | belum dipin | cardData.license apache-2.0. siblings berisi model.safetensors. Kandidat mode penuh, opsional. |
| `HuggingFaceTB/SmolLM2-135M-Instruct` | 12, 13, 14, 15 | Apache-2.0 | model.safetensors | belum dipin | cardData.license apache-2.0. siblings berisi model.safetensors. Kandidat mode cepat untuk LoRA, jalur GGUF, model jawaban modul 14, dan agen bila perlu model. |
| `Qwen/Qwen2.5-0.5B-Instruct` | 12, 13 | Apache-2.0 | model.safetensors | belum dipin | cardData.license apache-2.0. siblings berisi model.safetensors. Kandidat mode penuh yang opsional di MyLegion7i. |

Adapter, indeks vektor, dan berkas GGUF tidak masuk repo dan tidak di-push ke Hugging Face. Ollama hanya mengikat 127.0.0.1.
