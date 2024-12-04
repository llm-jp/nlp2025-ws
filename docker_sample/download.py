"""
Hugging Face Hubのモデルをダウンロードして、ローカルに保存する
"""

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("llm-jp/llm-jp-3-13b-instruct")
model = AutoModelForCausalLM.from_pretrained("llm-jp/llm-jp-3-13b-instruct")

# Save the model
model.save_pretrained("./models/llm-jp/llm-jp-3-13b-instruct")
tokenizer.save_pretrained("./models/llm-jp/llm-jp-3-13b-instruct")
