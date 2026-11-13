"""Unduh model dasar hanya bila mode jaringan dinyalakan.

Mode cepat tidak memanggil fungsi di berkas ini.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from muat_hf import muat_model, pastikan_boleh_unduh

ID_DASAR = "HuggingFaceTB/SmolLM2-135M-Instruct"
ID_PENUH = "Qwen/Qwen2.5-0.5B-Instruct"


def muat_dasar():
    pastikan_boleh_unduh()
    from transformers import AutoModelForCausalLM

    return muat_model(ID_DASAR, AutoModelForCausalLM)


def muat_penuh():
    pastikan_boleh_unduh()
    from transformers import AutoModelForCausalLM

    return muat_model(ID_PENUH, AutoModelForCausalLM)
