"""Unduh model kecil hanya bila mode jaringan dinyalakan.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import muat_model

ID_CEPAT = "HuggingFaceTB/SmolLM2-135M-Instruct"
ID_PENUH = "Qwen/Qwen2.5-0.5B-Instruct"


def muat_smol():
    return muat_model(ID_CEPAT)


def muat_qwen():
    return muat_model(ID_PENUH)
