"""Unduh model hanya bila A2N_UNDUH=1.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import muat_model, pastikan_boleh_unduh

ID_EMBEDDING = "sentence-transformers/all-MiniLM-L6-v2"
ID_JAWABAN = "HuggingFaceTB/SmolLM2-135M-Instruct"


def muat_embedding():
    pastikan_boleh_unduh()
    return muat_model(ID_EMBEDDING)


def muat_jawaban():
    pastikan_boleh_unduh()
    from transformers import AutoModelForCausalLM

    return muat_model(ID_JAWABAN, AutoModelForCausalLM)
