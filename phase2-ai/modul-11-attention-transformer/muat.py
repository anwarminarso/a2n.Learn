"""Unduh model klasifikasi kecil hanya bila mode jaringan dinyalakan.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import POLA_UNDUH, REVISI, pastikan_boleh_unduh

ID_PENUH = "google/bert_uncased_L-2_H-128_A-2"
ID_OPSIONAL = "distilbert/distilbert-base-uncased"


def _muat(model_id):
    pastikan_boleh_unduh()
    from huggingface_hub import snapshot_download
    from transformers import AutoModel, AutoTokenizer

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


def muat_bert_kecil():
    return _muat(ID_PENUH)


def muat_distilbert():
    return _muat(ID_OPSIONAL)
