# NLP2025ワークショップ「大規模言語モデルのファインチューニング技術と評価」

チューニングコンペティション参加者向けスクリプト

## チューニング用スクリプト

チューニングによるベースラインモデルの構築方法につきましては、[tuning-competition-baseline](https://github.com/llm-jp/tuning-competition-baseline)をご覧ください。

## Dockerイメージ構築用スクリプト

本コンペティションでは、最終成果としてモデルパラメーターと推論用コードを内包したDockerイメージの提出をお願いしております。 
Dockerイメージの構築方法につきましては、[docker_sample](https://github.com/llm-jp/nlp2025-ws/tree/main/docker_sample)をご覧ください。  

## 評価用スクリプト

本コンペティションの中間・最終評価に使われるスクリプトの一部を、[eval_script](https://github.com/llm-jp/eval_script)にて公開いたします。
ただし、評価に対するハックを防ぐため評価に使うプロンプトなどは含まれていません。
詳細につきましては[eval_script](https://github.com/llm-jp/eval_script)のREADMEをご覧ください。