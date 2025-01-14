import os
import json
import argparse
from vllm import LLM

# see more examples at https://github.com/vllm-project/vllm/tree/main/examples
chat_template = "{{ (messages|selectattr('role', 'equalto', 'system')|list|last).content|trim if (messages|selectattr('role', 'equalto', 'system')|list) else '' }}\n\n{% for message in messages %}\n{% if message['role'] == 'user' %}\n{{ message['content']|trim -}}\n{% if not loop.last %}\n\n\n{% endif %}\n{% elif message['role'] == 'assistant' %}\n{{ message['content']|trim -}}\n{% if not loop.last %}\n\n\n{% endif %}\n{% elif message['role'] == 'user_context' %}\n{{ message['content']|trim -}}\n{% if not loop.last %}\n\n\n{% endif %}\n{% endif %}\n{% endfor %}\n"

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
        messages_list.append({"role": "user", "content": d["text"]})

    for i, m in enumerate(messages_list):
        output = llm.chat([m], chat_template=chat_template)
        data[i]["response"] = output[0].outputs[0].text.strip()

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    with open(args.output_path, "w", encoding="utf-8") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
