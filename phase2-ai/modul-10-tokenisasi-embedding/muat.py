"""Unduh embedding mini hanya bila mode jaringan dinyalakan.

Mode cepat tidak memanggil muat_embedding.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import POLA_UNDUH, REVISI, pastikan_boleh_unduh

ID_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def muat_embedding():
    pastikan_boleh_unduh()
    from huggingface_hub import snapshot_download
    from transformers import AutoModel, AutoTokenizer

    model_id = ID_MODEL
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
    model = AutoModel.from_pretrained(
        folder,
        revision=revisi,
        use_safetensors=True,
        trust_remote_code=False,
        local_files_only=True,
    )
    return tokenizer, model
