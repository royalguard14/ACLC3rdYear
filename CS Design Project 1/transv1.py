from transformers import MarianMTModel, MarianTokenizer
import torch

# Define the model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-ar-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def preprocess_input(input_text):
    # Tokenize the input text
    tokenized_text = tokenizer.prepare_seq2seq_batch([input_text], return_tensors='pt')
    return tokenized_text

def encode_input(tokenized_text):
    # Encode the input text
    encoded_states = model.get_encoder()(input_ids=tokenized_text.input_ids, attention_mask=tokenized_text.attention_mask)
    return encoded_states

def decode_states(encoded_states, tokenized_text):
    # Generate translation
    translated_tokens = model.generate(**tokenized_text)
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]
    return translated_text

def postprocess_output(translated_text):
    # Detokenize and normalize the translated text
    final_output = translated_text[0]
    return final_output

# Example input text
input_text = "مرحبا بك في عالم الترجمة"
tokenized_text = preprocess_input(input_text)
encoded_states = encode_input(tokenized_text)
translated_text = decode_states(encoded_states, tokenized_text)
final_output = postprocess_output(translated_text)

print("Translated Output:", final_output)
