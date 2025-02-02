import pandas as pd
from fuzzywuzzy import process
import re
from transformers import pipeline
import torch

MEDICAL_PROMPT = (
    "You are a helpful medical assistant. Provide accurate, safe, and concise advice for health symptoms. "
    "Answer briefly and clearly.\n"
    "User: {query}\n"
    "Assistant:"
)

def get_ai_response(query):
    try:

        generator = pipeline(
            "text-generation",
            model="distilgpt2",  
            torch_dtype=torch.float16,
            device=0 if torch.cuda.is_available() else -1
        )
        print(f"Query received: {query}")
        
        prompt = MEDICAL_PROMPT.format(query=query)
        response = generator(
            prompt,
            max_length=150,           
            num_return_sequences=1,
            temperature=0.7,          
            top_p=0.9,                
            repetition_penalty=1.2,   
            do_sample=True
        )

        generated_text = response[0].get('generated_text', '')
        
        if "Assistant:" in generated_text:
            ai_response = generated_text.split("Assistant:")[-1].strip()
        else:
            ai_response = generated_text.strip()
        
        if not ai_response:
            ai_response = "I'm sorry, I could not generate an appropriate response."
        
        return (ai_response, None)
    except Exception as e:
        return (f"Error generating response: {str(e)}", None)
