import pandas as pd
from fuzzywuzzy import process
import re
from transformers import pipeline
import torch

# Updated medical prompt: instruct the model to answer concisely.
MEDICAL_PROMPT = (
    "You are a helpful medical assistant. Provide accurate, safe, and concise advice for health symptoms. "
    "Answer briefly and clearly.\n"
    "User: {query}\n"
    "Assistant:"
)

def get_ai_response(query):
    try:
        # Initialize the text-generation pipeline
        generator = pipeline(
            "text-generation",
            model="distilgpt2",  # Consider switching to a larger/fine-tuned model if possible.
            torch_dtype=torch.float16,
            device=0 if torch.cuda.is_available() else -1
        )
        print(f"Query received: {query}")
        
        # Format the prompt with the user query
        prompt = MEDICAL_PROMPT.format(query=query)
        response = generator(
            prompt,
            max_length=150,           # Limit the length to keep the response concise.
            num_return_sequences=1,
            temperature=0.7,          # Moderate temperature for balanced creativity.
            top_p=0.9,                # Use nucleus sampling to promote diversity.
            repetition_penalty=1.2,   # Penalize repetition.
            do_sample=True
        )
        # Extract generated text
        generated_text = response[0].get('generated_text', '')
        
        # Remove the prompt part if it's still present in the output.
        if "Assistant:" in generated_text:
            ai_response = generated_text.split("Assistant:")[-1].strip()
        else:
            ai_response = generated_text.strip()
        
        # Fallback in case no response was generated
        if not ai_response:
            ai_response = "I'm sorry, I could not generate an appropriate response."
        
        return (ai_response, None)
    except Exception as e:
        return (f"Error generating response: {str(e)}", None)
