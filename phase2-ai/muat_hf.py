"""Konstanta unduhan Hugging Face untuk Fase 2.

Mode cepat tidak memanggil muat_model. SHA di sini sama dengan
docs/lisensi-model.md. Modul 12, 13, 14, dan 15 memakai muat_model.
Embedding modul 14 (MiniLM) membiarkan kelas kosong, jadi yang terpakai
AutoModel. Model jawaban modul 14 serta modul 12, 13, dan 15
(SmolLM2 atau Qwen, model bahasa kausal) mengirim AutoModelForCausalLM.
Modul 10 dan 11 memuat AutoModel sendiri. Setiap pemuat memanggil
pastikan_boleh_unduh sebelum impor yang berat.
"""

import os

POLA_UNDUH = (
    "*.safetensors",
    "config.json",
    "generation_config.json",
    "tokenizer.json",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "vocab.txt",
    "merges.txt",
    "vocab.json",
)

REVISI = {
    "sentence-transformers/all-MiniLM-L6-v2": "1110a243fdf4706b3f48f1d95db1a4f5529b4d41",
    "google/bert_uncased_L-2_H-128_A-2": "30b0a37ccaaa32f332884b96992754e246e48c5f",
    "distilbert/distilbert-base-uncased": "12040accade4e8a0f71eabdb258fecc2e7e948be",
    "HuggingFaceTB/SmolLM2-135M-Instruct": "12fd25f77366fa6b3b4b768ec3050bf629380bac",
    "Qwen/Qwen2.5-0.5B-Instruct": "7ae557604adf67be50417f59c2c2f167def9a775",
}


def pastikan_boleh_unduh():
    """Tolak unduhan bila A2N_UNDUH bukan "1".

    Dipanggil sebelum impor huggingface_hub, transformers, atau torch.
    """
    if os.environ.get("A2N_UNDUH") != "1":
        raise RuntimeError("Unduhan hanya bila A2N_UNDUH=1")


def muat_model(model_id, kelas=None):
    """Muat tokenizer dan model dari salinan lokal.

    Bila kelas tidak diisi, yang dipakai AutoModel. Embedding modul 14
    (MiniLM) memakai bawaan itu. Model jawaban modul 14 serta modul 12,
    13, dan 15 (SmolLM2 atau Qwen, model bahasa kausal) mengirim
    AutoModelForCausalLM supaya kepala bahasa ikut termuat.
    """
    pastikan_boleh_unduh()
    from huggingface_hub import snapshot_download
    from transformers import AutoModel, AutoTokenizer

    if kelas is None:
        kelas = AutoModel
    revisi = REVISI[model_id]
    folder = snapshot_download(
        repo_id=model_id,
        revision=revisi,
        allow_patterns=POLA_UNDUH,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        folder,
        revision=revisi,
        trust_remote_code=False,
        local_files_only=True,
    )
    model = kelas.from_pretrained(
        folder,
        revision=revisi,
        use_safetensors=True,
        trust_remote_code=False,
        local_files_only=True,
    )
    return tokenizer, model
