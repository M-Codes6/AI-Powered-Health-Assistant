from fuzzywuzzy import process
import re

def process_symptoms(user_input, df_health):
    try:

        user_input = re.sub(r'[^a-zA-Z, ]', '', user_input).lower()
        symptoms = [s.strip() for s in re.split(r',| and |\&', user_input) if s.strip()]
        
        matched_symptoms = []
        advice_list = []
        
        for symptom in symptoms:
            match, score = process.extractOne(
                symptom,
                df_health['Symptom'].str.lower().tolist(),
                score_cutoff=75
            )
            if match:
                matched_symptoms.append(match)
                advice = df_health.loc[
                    df_health['Symptom'].str.lower() == match,
                    'Advice'
                ].values[0]
                advice_list.append(advice)
        
        if not matched_symptoms:

            return [], "Sorry, I couldn't find advice based on your input. Let me check with AI."
        
        return (
            list(set(matched_symptoms)),
            "\n".join(advice_list) if advice_list else ""
        )
        
    except Exception as e:
        return [], f"Error processing symptoms: {str(e)}"
