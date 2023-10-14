import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained("cerebras/Cerebras-GPT-590M")
model = AutoModelForCausalLM.from_pretrained("cerebras/Cerebras-GPT-590M")


while True:
    text = input("Introduce tu consulta: ")
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, num_beams=5, 
                            max_new_tokens=50, early_stopping=True,
                            no_repeat_ngram_size=2)
    text_output = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    print(text_output[0])