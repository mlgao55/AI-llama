from transformers import AutoTokenizer, AutoModelForCausalLM, MarianMTModel, MarianTokenizer
import torch

# Load the Llama model for reading
llama_model_name = "meta-llama/Llama-2-7b-chat-hf"
llama_tokenizer = AutoTokenizer.from_pretrained(llama_model_name)
llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name)

# Load translation models
translation_model_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')
translation_tokenizer_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')
translation_model_zh = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-zh')
translation_tokenizer_zh = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-zh')

# Ensure the models are on the correct device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
llama_model.to(device)
translation_model_es.to(device)
translation_model_zh.to(device)

# Function to read input file
def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
      
# Function to translate text
def translate_text(text, tokenizer, model, device):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return translated_text
  
# Read input text from file
input_file_path = './answer.txt'  # Replace with your input file path
input_text = read_input_file(input_file_path)

# Translate the text
translated_text_es = translate_text(input_text, translation_tokenizer_es, translation_model_es, device)
translated_text_zh = translate_text(input_text, translation_tokenizer_zh, translation_model_zh, device)

# Save the translated texts to files
output_file_path_spanish = 'translated_text_spanish.txt'  # Replace with your output file path
output_file_path_chinese = 'translated_text_chinese.txt'  # Replace with your output file path

with open(output_file_path_spanish, 'w', encoding='utf-8') as file:
    file.write(f"Translated text in Spanish:\n{translated_text_es}")

with open(output_file_path_chinese, 'w', encoding='utf-8') as file:
    file.write(f"Translated text in Chinese:\n{translated_text_zh}")

# Optionally display the translated texts
print(f"Translated text in Spanish:\n{translated_text_es}")
print(f"Translated text in Chinese:\n{translated_text_zh}")
