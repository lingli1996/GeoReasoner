from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
from peft import AutoPeftModelForCausalLM, PeftModel
import torch
import os
import json
from tqdm import tqdm
import time

def infer_model(model_path="./Qwen-VL-Models/Qwen-VL-Chat"):
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="cuda", trust_remote_code=True).eval()
    
    lora_weights = "./LoRA/train_reason"
    model = PeftModel.from_pretrained(model, lora_weights, torch_dtype=torch.bfloat16)
    lora_weights = "./LoRA/train_loc"
    model = PeftModel.from_pretrained(model, lora_weights, torch_dtype=torch.bfloat16)

    model.generation_config = GenerationConfig.from_pretrained(model_path, trust_remote_code=True)

    img_path = "/mnt/data/projects/Qwen-VL/add_cases/test.jpeg"

    query = tokenizer.from_list_format([
                {'image': img_path}, 
                {'text': "According to the content of the image, please think step by step and deduce in which country and city the image is most likely located and offer possible explanations. Output in JSON format, e.g., {'country': '', 'city': '' ,'reasons':''}."}
                ])
    
    response, history = model.chat(tokenizer, query=query, history=None)
    print(img_path, response)

if __name__ == "__main__":
    infer_model()