"""
Hugging Face Hubのモデルをダウンロードして、ローカルに保存する
"""

import argparse
from huggingface_hub import snapshot_download

parser = argparse.ArgumentParser()
parser.add_argument("model_name", type=str, default="llm-jp/llm-jp-3-13b-instruct")
args = parser.parse_args()

snapshot_download(
    repo_id=args.model_name,
    revision="main",
    local_dir=f"./models/{args.model_name}",
    local_dir_use_symlinks=False
)
