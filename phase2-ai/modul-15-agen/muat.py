"""Unduh model bahasa hanya bila A2N_UNDUH=1.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import muat_model

ID_AGEN = "HuggingFaceTB/SmolLM2-135M-Instruct"


def _jaga():
    if os.environ.get("A2N_UNDUH") != "1":
        raise RuntimeError("Unduhan hanya bila A2N_UNDUH=1")


def muat_agen():
    _jaga()
    from transformers import AutoModelForCausalLM

    return muat_model(ID_AGEN, AutoModelForCausalLM)
