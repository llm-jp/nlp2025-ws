import os
import json
import time
from argparse import ArgumentParser

from openai import AzureOpenAI, OpenAIError
import pandas as pd
from math_equivalence import is_equiv

class safe_eval:
    def __init__(self):
        self.client: AzureOpenAI = AzureOpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            api_version=os.environ["OPENAI_API_VERSION"],
            azure_endpoint=os.environ["OPENAI_API_BASE"],
        )
        self.sys_prompt: str = "add YOUR_SYSTEM_PROMPT_IF_YOU_NEED"
        self.prompt: str = "add YOUR_PROMPT_FOR_LLM_AS_A_JUDGE which should includes {question}, {reference_answer}, and {answer}"
        self.hyperparameters: dict = {
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
            "temperature": 0.0,
            "top_p": 0.0
        }

    def run(self, input: dict) -> int:
        question = input['text']
        answer = input['response']
        reference_answer = input['gold'] if input['gold'] else ""

        query_str: str = self.prompt.format(question=question, reference_answer=reference_answer, answer=answer)

        message = [
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": query_str},
        ]

        try:
            response = self.client.chat.completions.create(
                model=os.environ["OPENAI_API_MODEL"],
                messages=message,
                frequency_penalty=self.hyperparameters["frequency_penalty"],
                max_tokens=2048,
                presence_penalty=self.hyperparameters["presence_penalty"],
                temperature=self.hyperparameters["temperature"],
                top_p=self.hyperparameters["top_p"],
            )
            time.sleep(1)
        except OpenAIError:
            return -1

        label: int = -1
        if response.choices[0].finish_reason == "stop":
            label = response.choices[0].message.content

        return label

class math_eval:
    def __init__(self):
        return 1

    def run(self, input: dict) -> int:
        return 1 if is_equiv(input['gold'].strip(), input['response'].strip()) else 0

def main(args):
    if args.target_task == "math":
        evaluator = math_eval()
    elif args.target_task == "safe":
        evaluator = safe_eval()
    else:
        print("not support task")
        return 0

    scores = { "all": [] }
    for line in open(args.input_file):
        tmp = json.loads(line.strip())
        score = evaluator.run(tmp)
        if tmp['type'] not in scores:
            scores[tmp['type']] = []
        scores[tmp['type']].append(score)
        scores['all'].append(score)
    for q_type in scores:
        scores[q_type] = sum(scores[q_type]) / len(scores[q_type])
    
    scores = scores.items()

    team_column = []
    task_column = []
    cat_column = []
    score_column = []
    type_column = []

    for q_type, score in scores:
        team_column.append(args.anonymized_name)
        task_column.append(args.target_task)
        cat_column.append(q_type)
        score_column.append(score)
        type_column.append(args.evaluation_split)

    data = {
        'チーム名': team_column,
        'タスク': task_column,
        'カテゴリー': cat_column,
        'スコア': score_column,
        'データタイプ': type_column
    }

    df = pd.DataFrame(data)
    df.to_csv(args.output_file, index=False)

    return 1

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-e", "--evaluation-split", type=str, required=True)
    parser.add_argument("-i", "--input-file", type=str, required=True)
    parser.add_argument("-n", "--team-name", type=str, required=True)
    parser.add_argument("-o", "--output-file", type=str, required=True)
    parser.add_argument("-t", "--target-task", choices=['math', 'safe'], required=True)
    args = parser.parse_args()

    main(args)
