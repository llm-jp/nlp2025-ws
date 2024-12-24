# 結果提出用Dockerイメージ構築例

NLP2025ワークショップ２：「大規模言語モデルのファインチューニング技術と評価」では、評価時にモデルパラメーターと推論用スクリプトを含んだDockerイメージを提出いただきます。  
モデルパラメーターのチューニング及び、本スクリプトの`src/main.py`を編集する形でシステムを開発いただくことを想定しています。

## 事前準備

### Dockerインストール

計算環境にDockerを[インストール](https://docs.docker.com/engine/install/)してください。

### モデルダウンロード

Huggig Face Hubから`llm-jp/llm-jp-3-1.8b-instruct`をローカルに保存します。  

> [!NOTE]
> 本例では、1.8Bモデルを使用しますが、適宜3.7Bモデル、13Bモデルに置き換えてご使用ください。  
> 別のモデルを使用する場合、手元のモデルのパスを`./Dockerfile`に設定してください。

```
python3 -m venv venv
venv/bin/pip3 install transformers
venv/bin/python3 download.py
```

## Dockerイメージの保存

### ビルド

`./Dockerfile`からDockerイメージをビルドします。  
この際、`./src`以下のスクリプトと、`Dockerfile`内で指定したモデルパラメーターがDockerコンテナ内に転送されます。  

> [!NOTE]
> `[チーム名]`は適宜置き換えてください。

```
docker build . -t [チーム名]
```

### 保存

Dockerイメージをローカルに保存します。

```
docker save [チーム名] > [チーム名].tar
```

最終評価では`[チーム名].tar`を提出してください。

## 動作検証

実際に提出したDockerイメージが想定通り動くかどうか以下の手順でテストすることができます。

**TBA**
