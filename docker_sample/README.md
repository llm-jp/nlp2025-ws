# 結果提出用Dockerサンプル

NLP2025ワークショップ２：「大規模言語モデルのファインチューニング技術と評価」の結果提出用サンプルスクリプトです。  
本ワークショップではモデルパラメーターと推論用スクリプトを含んだDockerイメージを提出いただきます。  

## 事前準備

### モデルダウンロード

Huggig Face Hubから`llm-jp/llm-jp-3-13b-instruct`をローカルに保存します。  

> [!NOTE]
> 別のモデルを使用する場合は、この手順は必要ありません。
> その場合、`./Dockerfile`内のパスを修正してください。

```
python3 -m venv venv
venv/bin/pip3 install transformers
venv/bin/python3 download.py
```

## Dockerイメージの保存

### ビルド

`./Dockerfile`からDockerイメージをビルドします。  
この際、`./src`以下のスクリプトと、モデルパラメーターがDockerコンテナ内に転送されます。  

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