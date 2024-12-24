# 結果提出用Dockerイメージ構築例

NLP2025ワークショップ２：「大規模言語モデルのファインチューニング技術と評価」で開催されるチューニングコンペティションでは、評価時にモデルパラメーターと推論用スクリプトを含んだDockerイメージを提出いただきます。  
本コンペティションでは、モデルパラメーターのチューニング及び、本スクリプトの`src/main.py`を編集する形でシステムを開発いただくことを想定しています。

## 事前準備

### Dockerインストール

計算環境にDockerを[インストール](https://docs.docker.com/engine/install/)してください。

### モデルダウンロード

Huggig Face Hubから`llm-jp/llm-jp-3-1.8b-instruct`をローカルに保存します。  

> [!NOTE]
> 本例では、1.8Bモデルを使用しますが、適宜3.7Bモデル、13Bモデルに置き換えてご使用ください。  
> 別のモデルを用いる場合は、`./Dockerfile`のモデルパスを編集してください。

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

```bash
docker run --rm \
  --runtime=nvidia \
  --gpus all \
  --network none \
  -v "$(pwd)/data:/data" \
  -e INPUT_PATH=/data/input.jsonl \
  -e OUTPUT_PATH=/data/output.jsonl \
  [チームID]
```

### ビルドしたイメージの削除

```
sudo docker rmi [チームID]
```