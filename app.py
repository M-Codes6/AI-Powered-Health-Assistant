import streamlit as st
import pandas as pd
from models import get_ai_response
from symptom_processor import process_symptoms

st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="🧳")

st.markdown("""
    <style>
            
        /* Hide the entire toolbar containing Share, GitHub, etc. */
    .stToolbarActions { 
        display: none !important; 
    }
            
    /* Backgrounds */
    .reportview-container {
        background-color: #F5F7FB;
    }
    .dark .reportview-container {
        background-color: #0A0E14;
    }
    
    /* Default styles for title and subheader */
    h1 {
        text-align: center;
        font-size: 1.2rem;
        opacity: 0.6;
    }
    h3 {
        text-align: center;
        font-size: 1rem;
        opacity: 0.5;
    }
    @media (max-width: 480px) {
        h1 {
            font-size: 1rem;
        }
        h3 {
            font-size: 0.9rem;
        }
    }
    
    /* Input Fields */
    .stTextInput > div, .stNumberInput > div {
        max-width: 300px !important;
    }
    .stTextInput input, .stNumberInput input {
        border-radius: 8px !important;
        border: 1px solid #1A1A1A !important;
        padding: 10px 12px !important;
        font-size: 0.95rem !important;
    }
    .dark .stTextInput input, .dark .stNumberInput input {
        background-color: #2D2D2D !important;
        border: 1px solid #404040 !important;
        color: #E0E0E0 !important;
    }
    
    /* Text Area */
    .stTextArea textarea {
        min-height: 70px !important;
        border-radius: 15px !important;
    }
    
    /* Containers */
    .stContainer {
        border-radius: 12px;
        padding: 1.5rem;
        background-color: #FFFFFF;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .dark .stContainer {
        background-color: #1A1A1A;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
            
    
            
    /* Buttons */
    .stButton button {
        background-color: #2A9D8F !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        transition: all 0.3s ease;
        font-weight: 500 !important;
    }
    .stButton button:hover {
        background-color: #21867A !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dark .stButton button {
        background-color: #3DB4A4 !important;
    }
    
    /* Footer links */
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 0.9rem;
    }
    .footer a {
        color: #0077b6;
        text-decoration: none;
        margin: 0 10px;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧳AI-Powered Health Assistant")
st.subheader("How can I assist you today?")

@st.cache_data
def load_health_data():
    try:
        return pd.read_csv("health_data.csv", quoting=1)
    except Exception as e:
        st.error(f"Error loading health data: {str(e)}")
        return None

user_input = st.text_area(
    "",
    placeholder="Describe your symptoms or ask about health/fitness advice...",
    height=120,
    key="user_input"
)

if st.button("Send", key="query_button"):
    if user_input.strip():
        st.markdown("### **Response:**")
        with st.spinner("Processing..."):
            df_health = load_health_data()
            if df_health is not None:
                detected_symptoms, advice = process_symptoms(user_input, df_health)

                if detected_symptoms and advice != "Sorry, I couldn't find advice based on your input. Let me check with AI.":
                    st.markdown(f"**Detected Symptoms:** {', '.join(detected_symptoms)}")
                    st.markdown("**Recommendation:**")
                    st.success(advice)
                else:

                    ai_response, _ = get_ai_response(user_input)
                    st.markdown("**AI-Generated Advice:**")
                    st.success(ai_response)
            else:
                st.warning("Symptom database not available. Using AI response only.")
                ai_response, _ = get_ai_response(user_input)
                st.success(ai_response)
        st.markdown("---\n*Remember: This is not medical advice. Always consult a professional doctor for serious concerns.*")
    else:
        st.warning("Please enter your symptoms or question.")


# Fitness tracking section

st.markdown("### **Fitness Tracking: Calculate Your BMI**")
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.1f", key="weight_input")
height_unit = st.selectbox("Select your height unit:", ["Meters", "Centimeters", "Feet/Inches"], key="height_unit_select")

height = 0.0
if height_unit == "Meters":

    height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f", key="height_meters_input")
elif height_unit == "Centimeters":

    height_cm = st.number_input("Enter your height (cm):", min_value=50, max_value=300, format="%d", key="height_cm_input")
    height = height_cm / 100  
else:  

    feet = st.number_input("Feet:", min_value=0, max_value=9, step=1, format="%d", key="feet_input")
    inches = st.number_input("Inches:", min_value=0, max_value=11, step=1, format="%d", key="inches_input")
    if feet == 0 and inches == 0:
        st.warning("Height cannot be zero.")
    else:
        height = (feet * 0.3048) + (inches * 0.0254)

if st.button("Calculate BMI", key="bmi_button"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.1f}")
        if bmi < 18.5:
            st.info("Underweight 🚨: Consider a balanced diet and consult a healthcare professional.")
        elif 18.5 <= bmi < 25:  # Fixed range
            st.success("Normal weight ✅: Keep up the great work!")
        elif 25 <= bmi < 30:  # Fixed range
            st.warning("Overweight ⚠️: Regular exercise and a balanced diet can help.")
        else:
            st.error("Obese ❗: Consult a healthcare professional for personalized advice.")
    else:
        st.warning("Please enter valid weight and height.")

st.caption("Stay safe and healthy! ✨")

# Footer Section 
st.markdown("""
    <div class="footer">
        <p>
            <a href="https://x.com/M_Codes6" target="_blank">X</a> | 
            <a href="https://github.com/M-Codes6" target="_blank">Github</a> | 
            <a href="mailto:naikmuzamil06@gmail.com" target="_blank">G-mail</a>
        </p>
    </div>
""", unsafe_allow_html=True)
























# Updated BMI Section with Height Selection
st.markdown("### **Fitness Tracking: Calculate Your BMI**")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.1f")

# Dropdown to select height unit
height_unit = st.selectbox("Select your height unit:", ["Meters", "Centimeters", "Feet/Inches"])

if height_unit == "Meters":
    height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")
elif height_unit == "Centimeters":
    height_cm = st.number_input("Enter your height (cm):", min_value=50, max_value=300, format="%d")
    height = height_cm / 100  # Convert centimeters to meters
else:  # Feet/Inches
    feet = st.number_input("Feet:", min_value=0, max_value=9, step=1, format="%d")
    inches = st.number_input("Inches:", min_value=0, max_value=11, step=1, format="%d")
    height = (feet * 0.3048) + (inches * 0.0254)  # Convert feet and inches to meters

if st.button("Calculate BMI", key="bmi_button"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            st.info("You are underweight. Consider a balanced diet and consult a healthcare professional.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight. Keep up the great work!")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight. Regular exercise and a balanced diet can help.")
        else:
            st.error("You are obese. Please consult a healthcare professional for personalized advice.")
    else:
        st.warning("Please enter valid weight and height.")
