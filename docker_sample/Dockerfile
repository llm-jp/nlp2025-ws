# ベースイメージの指定
FROM nvcr.io/nvidia/pytorch:24.08-py3

# 作業ディレクトリの設定
WORKDIR /workspace

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# vLLMのインストール
RUN pip install --no-cache-dir vllm nvidia-ml-py && \
    pip uninstall --yes pynvml && \
    pip install -U --no-cache-dir opencv-python-headless==4.5.5.62

# モデルファイルをイメージに取り込む (FIXME: モデルファイルのパスを変更)
COPY ./models/llm-jp/llm-jp-3-1.8b-instruct /workspace/model

# ソースコードをイメージに取り込む
COPY ./src /workspace/src

# コンテナ起動時のコマンド設定
CMD ["entrypoint.sh"]

# エントリーポイントスクリプトの作成
RUN echo -e '#!/bin/bash\npython3 src/main.py ./model --input_path ${INPUT_PATH} --output_path ${OUTPUT_PATH}' > \
    /usr/local/bin/entrypoint.sh && \
    chmod +x /usr/local/bin/entrypoint.sh
