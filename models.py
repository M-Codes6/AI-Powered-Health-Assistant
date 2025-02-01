import pandas as pd
from transformers import pipeline
import torch
import re
from fuzzywuzzy import process

health_data = pd.read_csv('health_data.csv')

health_data.columns = health_data.columns.str.lower()

MEDICAL_PROMPT = """You are a medical assistant. Provide accurate, safe, and concise advice for health symptoms.
User: {query}
Assistant:"""

def get_ai_response(query):
    try:
        generator = pipeline(
            "text-generation",
            model="distilgpt2",  
            torch_dtype=torch.float16,
            device=0 if torch.cuda.is_available() else -1
        )

        print(f"Query received: {query}")
        
        query_clean = re.sub(r'[^a-zA-Z\s]', '', query).lower()  
        symptoms_in_query = re.split(r'\s+|,| and |&', query_clean)  
        
        print(f"Cleaned user input: {query_clean}")
        
        matched_symptoms = []
        advice_list = []
        
        for symptom in symptoms_in_query:
            if symptom:  
                match, score = process.extractOne(
                    symptom,
                    health_data['symptom'].str.lower().tolist(),
                    score_cutoff=70  
                )
                if match:
                    matched_symptoms.append(match)

                    advice = health_data.loc[
                        health_data['symptom'].str.lower() == match,
                        'advice'
                    ].values[0]
                    advice_list.append(advice)

        if matched_symptoms:

            return (
                list(set(matched_symptoms)), 
                "\n".join(advice_list)  
            )
        
        print("No match found in CSV, using AI model...")
        response = generator(
            MEDICAL_PROMPT.format(query=query),
            max_length=200,
            num_return_sequences=1,
            temperature=0.3,
            do_sample=True,
        )
        
        ai_response = response[0]['generated_text'].split("Assistant:")[-1].strip()
        
        return ai_response, None

    except Exception as e:
        return f"Error generating response: {str(e)}", None
