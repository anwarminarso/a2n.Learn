# Register lisensi model

Revisi dipin pada 2026-11-13 dari `https://huggingface.co/api/models/<id>/revision/main`, tanpa mengunduh bobot. Kolom SHA adalah field `sha` pada respons itu. Lisensi dibaca dari `cardData.license` pada revisi yang sama. Daftar berkas di bawah adalah `siblings` pada revisi itu. Saat sebuah modul mengunduh, lisensi dan adanya berkas `.safetensors` sudah dicek pada revisi yang dipin, sebelum unduh.

Unduhan hanya boleh untuk model kecil berlisensi Apache-2.0 atau MIT yang punya berkas `.safetensors`, dengan `trust_remote_code=False`. `allow_patterns` hanya mengizinkan `*.safetensors`, `config.json`, `generation_config.json`, dan berkas tokenizer. Berkas pickle `pytorch_model.bin` dan `training_args.bin` tidak masuk pola itu, jadi tidak diunduh.

Kelima kandidat lolos dua syarat pada revisi yang dipin: `cardData.license` adalah `apache-2.0`, dan `siblings` berisi berkas `.safetensors`. Tidak ada model yang diganti.

`prajjwal1/bert-tiny` ditolak untuk mode cepat modul 11. `cardData.license` bertanda MIT. `siblings` berisi `pytorch_model.bin` dan tidak berisi berkas `.safetensors`. Id itu tidak masuk tabel.

Tidak ada kandidat di tabel yang lisensinya di luar Apache-2.0 atau MIT, dan tidak ada baris tanpa berkas safetensors. Kandidat baru yang lisensinya lain, atau yang tidak punya `.safetensors`, tidak diunduh.

Modul 9 tidak mengunduh model. Jaringannya ditulis di materi.

README modul 12 dan 13 memakai SHA pada tabel ini. README modul 14 dan 15 masih placeholder. Kalimat status belum dipin di README itu belum diganti, karena isi modul itu belum ditulis.

| Model | Modul | Lisensi | SHA revisi | Dicek | Safetensors | Pickle yang dikecualikan |
|---|---|---|---|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | 10, 14 | Apache-2.0 | `1110a243fdf4706b3f48f1d95db1a4f5529b4d41` | 2026-11-13 | model.safetensors | `pytorch_model.bin` |
| `google/bert_uncased_L-2_H-128_A-2` | 11 | Apache-2.0 | `30b0a37ccaaa32f332884b96992754e246e48c5f` | 2026-11-13 | model.safetensors | `pytorch_model.bin` |
| `distilbert/distilbert-base-uncased` | 11 | Apache-2.0 | `12040accade4e8a0f71eabdb258fecc2e7e948be` | 2026-11-13 | model.safetensors | `pytorch_model.bin` |
| `HuggingFaceTB/SmolLM2-135M-Instruct` | 12, 13, 14, 15 | Apache-2.0 | `12fd25f77366fa6b3b4b768ec3050bf629380bac` | 2026-11-13 | model.safetensors | `training_args.bin` |
| `Qwen/Qwen2.5-0.5B-Instruct` | 12, 13 | Apache-2.0 | `7ae557604adf67be50417f59c2c2f167def9a775` | 2026-11-13 | model.safetensors | tidak ada `pytorch_model.bin` dan tidak ada `training_args.bin` |

Adapter, indeks vektor, dan berkas GGUF tidak masuk repo dan tidak di-push ke Hugging Face. Ollama hanya mengikat 127.0.0.1.

## Berkas pada revisi yang dipin

### `sentence-transformers/all-MiniLM-L6-v2`

SHA `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`. Repo ini juga memuat pickle `pytorch_model.bin`. Pola unduh kita tidak memuat berkas itu.

- `.gitattributes`
- `1_Pooling/config.json`
- `README.md`
- `config.json`
- `config_sentence_transformers.json`
- `data_config.json`
- `model.safetensors`
- `modules.json`
- `onnx/model.onnx`
- `onnx/model_O1.onnx`
- `onnx/model_O2.onnx`
- `onnx/model_O3.onnx`
- `onnx/model_O4.onnx`
- `onnx/model_qint8_arm64.onnx`
- `onnx/model_qint8_avx512.onnx`
- `onnx/model_qint8_avx512_vnni.onnx`
- `onnx/model_quint8_avx2.onnx`
- `openvino/openvino_model.bin`
- `openvino/openvino_model.xml`
- `openvino/openvino_model_qint8_quantized.bin`
- `openvino/openvino_model_qint8_quantized.xml`
- `pytorch_model.bin`
- `rust_model.ot`
- `sentence_bert_config.json`
- `special_tokens_map.json`
- `tf_model.h5`
- `tokenizer.json`
- `tokenizer_config.json`
- `train_script.py`
- `vocab.txt`

### `google/bert_uncased_L-2_H-128_A-2`

SHA `30b0a37ccaaa32f332884b96992754e246e48c5f`. Repo ini juga memuat pickle `pytorch_model.bin`. Pola unduh kita tidak memuat berkas itu.

- `.gitattributes`
- `README.md`
- `config.json`
- `flax_model.msgpack`
- `model.safetensors`
- `pytorch_model.bin`
- `vocab.txt`

### `distilbert/distilbert-base-uncased`

SHA `12040accade4e8a0f71eabdb258fecc2e7e948be`. Repo ini juga memuat pickle `pytorch_model.bin`. Pola unduh kita tidak memuat berkas itu.

- `.gitattributes`
- `LICENSE`
- `README.md`
- `config.json`
- `flax_model.msgpack`
- `model.safetensors`
- `pytorch_model.bin`
- `rust_model.ot`
- `tf_model.h5`
- `tokenizer.json`
- `tokenizer_config.json`
- `vocab.txt`

### `HuggingFaceTB/SmolLM2-135M-Instruct`

SHA `12fd25f77366fa6b3b4b768ec3050bf629380bac`. Repo ini juga memuat pickle `training_args.bin`. Pola unduh kita tidak memuat berkas itu. Tidak ada `pytorch_model.bin` pada revisi ini.

- `.gitattributes`
- `README.md`
- `all_results.json`
- `config.json`
- `eval_results.json`
- `generation_config.json`
- `merges.txt`
- `model.safetensors`
- `onnx/model.onnx`
- `onnx/model_bnb4.onnx`
- `onnx/model_fp16.onnx`
- `onnx/model_int8.onnx`
- `onnx/model_q4.onnx`
- `onnx/model_q4f16.onnx`
- `onnx/model_quantized.onnx`
- `onnx/model_uint8.onnx`
- `runs/Oct31_10-14-22_ip-26-0-174-36/events.out.tfevents.1730370128.ip-26-0-174-36.3239327.0`
- `runs/Oct31_10-14-22_ip-26-0-174-36/events.out.tfevents.1730376056.ip-26-0-174-36.3239327.1`
- `special_tokens_map.json`
- `tokenizer.json`
- `tokenizer_config.json`
- `train_results.json`
- `trainer_state.json`
- `training_args.bin`
- `vocab.json`

### `Qwen/Qwen2.5-0.5B-Instruct`

SHA `7ae557604adf67be50417f59c2c2f167def9a775`. Pada revisi ini tidak ada `pytorch_model.bin` dan tidak ada `training_args.bin`.

- `.gitattributes`
- `LICENSE`
- `README.md`
- `config.json`
- `generation_config.json`
- `merges.txt`
- `model.safetensors`
- `tokenizer.json`
- `tokenizer_config.json`
- `vocab.json`
