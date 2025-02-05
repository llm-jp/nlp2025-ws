# 評価用スクリプト例

ここではNLP2025ワークショップ２：「大規模言語モデルのファインチューニング技術と評価」で開催されるチューニングコンペティションに用いられる評価スクリプトの一部を公開いたします。

## 注意事項

評価スクリプト自体や評価に用いられるプロンプトなどに対するハックを防ぐため、このレポジトリーは一部の情報を削除して公開されています。
ここのスクリプトだけでは評価が難しいので、コードをご確認の上、必要な情報を記入・修正してからお使いになってください。

## 使い方

基本的な使用例は以下となります。

```
usage: eval.py [-h] -e EVALUATION_SPLIT -i INPUT_FILE -n TEAM_NAME -o OUTPUT_FILE -t {math,safe}

options:
  -h, --help            show this help message and exit
  -e EVALUATION_SPLIT, --evaluation-split EVALUATION_SPLIT
  -i INPUT_FILE, --input-file INPUT_FILE
  -n TEAM_NAME, --team-name TEAM_NAME
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
  -t {math,safe}, --target-task {math,safe}
```

- EVALUATION_SPLIT: 評価対象のデータに対する説明です。「第一回中間評価」、「最終評価」などになります。
- INPUT_FILE: Dockerイメージで生成された、何らかの回答が含まれている jsonl ファイルです
- TEAM_NAME: 参加チームの名前です。
- OUTPUT_FILE: 評価結果を出力するファイルの名前です。評価結果は csv の形式で出力されます。
- TARGET_TASK: math/safe の二択となります。

また、この評価スクリプトは LLM-as-a-Judge の際に、AzureOpenAI を用います。
以下の関係変数を事前に宣言してください。

```
echo "export OPENAI_API_KEY='yourapikey'"
echo "export OPENAI_API_VERSION='yourapiversion'"
echo "export OPENAI_API_BASE='yourapibase'"
echo "export OPENAI_API_MODEL='yourapimodel'"
```