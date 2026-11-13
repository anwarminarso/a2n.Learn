"""Unduh model hanya bila A2N_UNDUH=1.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import muat_model

ID_EMBEDDING = "sentence-transformers/all-MiniLM-L6-v2"
ID_JAWABAN = "HuggingFaceTB/SmolLM2-135M-Instruct"


def _jaga():
    if os.environ.get("A2N_UNDUH") != "1":
        raise RuntimeError("Unduhan hanya bila A2N_UNDUH=1")


def muat_embedding():
    _jaga()
    return muat_model(ID_EMBEDDING)


def muat_jawaban():
    _jaga()
    from transformers import AutoModelForCausalLM

    return muat_model(ID_JAWABAN, AutoModelForCausalLM)
