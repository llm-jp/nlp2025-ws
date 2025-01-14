import os
import json
import argparse
from vllm import LLM


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("model_path", type=str)
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    parser.add_argument("--num_gpus", type=int, default=1)

    args = parser.parse_args()

    llm = LLM(
        model=args.model_path,
        tensor_parallel_size=args.num_gpus,
    )

    with open(args.input_path, "r", encoding="utf-8") as f:
        data = list(map(json.loads, f))

    messages_list = []
    for d in data:
        messages = [{"role": "user", "content": d["text"]}]
        messages_list.append(messages)

    outputs = llm.chat(messages_list)
    for i, output in enumerate(outputs):
        data[i]["response"] = output.outputs[0].text

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    with open(args.output_path, "w", encoding="utf-8") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
