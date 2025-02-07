# 結果提出用Dockerイメージ構築例

NLP2025ワークショップ２：「大規模言語モデルのファインチューニング技術と評価」で開催されるチューニングコンペティションでは、モデルパラメーターと推論用スクリプトを含んだDockerイメージを提出いただきます。  
本コンペティションでは、モデルパラメーターのチューニング及び、本スクリプトの`src/main.py`を編集する形でシステムを開発いただくことを想定しています。

## 事前準備

### git clone

```bash
git clone https://github.com/llm-jp/nlp2025-ws.git
cd nlp2025-ws/docker_sample
```

### Dockerインストール

計算環境にDockerを[インストール](https://docs.docker.com/engine/install/)してください。

### モデルダウンロード

Huggig Face Hubから`llm-jp/llm-jp-3-1.8b-instruct`をローカルに保存します。  

> [!NOTE]
> 本例では、1.8Bモデルを使用しますが、適宜3.7Bモデル、13Bモデルに置き換えてご使用ください。  
> 別のモデルを用いる場合は`./Dockerfile`のモデルパスを編集してください。

```
python3 -m venv venv
venv/bin/pip3 install transformers
venv/bin/python3 download.py llm-jp/llm-jp-3-1.8b-instruct
```

## Dockerイメージの保存

### ビルド

`./Dockerfile`からDockerイメージをビルドします。  
この際、`./src`以下のスクリプトと、`Dockerfile`内で指定したモデルパラメーターがDockerコンテナ内に転送されます。  

> [!NOTE]
> `[チーム]`は適宜置き換えてください。

```
sudo docker build . -t [チームID]
```

### 保存

Dockerイメージをローカルに保存します。

```
sudo docker save [チームID] > [チームID].tar
```

最終評価では`[チームID].tar`を提出してください。

### ビルドしたイメージの削除

```
sudo docker rmi [チームID]
```

## 動作検証

実際に提出したDockerイメージが想定通り動くかどうか以下の手順でテストすることができます。

### 読み込み

ローカルに保存したDockerイメージを読み込みます。

```
sudo docker load < [チームID].tar
```

### Dockerイメージの起動

読み込んだDockerイメージを起動します。  
`./data/output.jsonl`が書き出されていれば成功です。

> [!WARNING]
> コンペティションの最終評価時には、以下の引数があらかじめ指定された状態で実行されます。  
> 任意の引数を追加・変更することはできませんので、あらかじめご了承ください。

```bash
docker run --rm \
  --gpus all \
  --network none \
  -v "$(pwd)/data:/data" \
  -e INPUT_PATH=/data/input.jsonl \
  -e OUTPUT_PATH=/data/output.jsonl \
  --shm-size 128g \
  [チームID]
```

ここでは、ローカルの`./data`をDockerコンテナ内の`/data`にマウントしています。  
`./data`にjsonlファイルを作成し、入力パス`INPUT_PATH=/data/input.jsonl`を編集することで任意の入力を処理できます。

### 読み込んだイメージの削除

```
sudo docker rmi [チームID]
```

## よくあるエラーと対処法

### ValueError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one

`src/main.py`は`vllm.LLM.chat`を使用しているため、使用する場合はchat-templateの登録が必要です。  
[chat_templating#how-do-i-create-a-chat-template](https://huggingface.co/docs/transformers/v4.47.1/ja/chat_templating#how-do-i-create-a-chat-template)を参考に、chat-templateを作成し、手元のモデルの`tokenizer_config.json`に追記してください。  
追記方法は、[llm-jp-3-1.8b-instruct/blob/main/tokenizer_config.json](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct/blob/main/tokenizer_config.json)を参考にしてください。  
