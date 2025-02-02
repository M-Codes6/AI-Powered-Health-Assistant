from fuzzywuzzy import process
import re

def process_symptoms(user_input, df_health):
    try:
        # Clean the input: allow only letters, commas, and spaces; then convert to lowercase
        user_input = re.sub(r'[^a-zA-Z, ]', '', user_input).lower()
        # Split the input into candidate symptom phrases
        symptoms = [s.strip() for s in re.split(r',| and |\&', user_input) if s.strip()]
        
        matched_symptoms = []
        advice_list = []
        
        # For each candidate symptom, attempt fuzzy matching with the CSV symptom list
        for symptom in symptoms:
            match, score = process.extractOne(
                symptom,
                df_health['Symptom'].str.lower().tolist(),
                score_cutoff=75
            )
            if match:
                matched_symptoms.append(match)
                # Retrieve the corresponding advice from the CSV
                advice = df_health.loc[
                    df_health['Symptom'].str.lower() == match,
                    'Advice'
                ].values[0]
                advice_list.append(advice)
        
        # If no symptom was matched, return an empty list and a fallback message
        if not matched_symptoms:
            return ([], "Sorry, I couldn't find advice based on your input. Let me check with AI.")
        
        # Otherwise, return the unique matched symptoms and the concatenated advice
        return (list(set(matched_symptoms)), "\n".join(advice_list) if advice_list else "")
        
    except Exception as e:
        return ([], f"Error processing symptoms: {str(e)}")
