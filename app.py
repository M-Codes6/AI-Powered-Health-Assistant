import streamlit as st
import pandas as pd
from models import get_ai_response
from symptom_processor import process_symptoms

st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="🧳")

# Custom CSS to handle both light and dark modes
st.markdown("""
    <style>
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
        min-height: 100px !important;
        border-radius: 10px !important;
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

    /* Messages and Alerts */
    .stSuccess {
        background-color: #D4EDDA !important;
        color: #155724 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    .dark .stSuccess {
        background-color: #1E4530 !important;
        color: #C3E6CB !important;
    }
    .stWarning {
        background-color: #FFF3CD !important;
        color: #856404 !important;
        padding: 1rem !important;
    }
    .dark .stWarning {
        background-color: #4D3F12 !important;
        color: #FFE082 !important;
    }
    .stError {
        background-color: #F8D7DA !important;
        color: #721C24 !important;
        padding: 1rem !important;
    }
    .dark .stError {
        background-color: #4A2326 !important;
        color: #F5C6CB !important;
    }

    /* Captions and Text */
    .stMarkdown {
        color: #4A4A4A;
        line-height: 1.6 !important;
    }
    .dark .stMarkdown {
        color: #D0D0D0;
    }
    .stCaption {
        color: #6C757D;
        font-size: 0.9rem !important;
    }
    .dark .stCaption {
        color: #A0A0A0;
    }

    /* Spacing Improvements */
    .stTextInput, .stNumberInput, .stTextArea {
        margin-bottom: 1rem !important;
    }
    .stButton {
        margin: 0.5rem 0 !important;
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


df_health = load_health_data()

user_input = st.text_area(
    "",
    placeholder="Describe your symptoms or ask about health/fitness advice...",
    height=120,
    key="user_input"
)

if st.button("Send", key="query_button"):
    if user_input.strip():
        st.markdown("### **AI Response:**")
        with st.spinner("processing..."):
            if df_health is not None:
                detected_symptoms, advice = process_symptoms(user_input, df_health)
                
                if detected_symptoms:
                    st.markdown(f"**Detected Symptoms:** {', '.join(detected_symptoms)}")
                    st.markdown("**Recommendation:**")
                    st.success(advice)
                else:
                    ai_response = get_ai_response(user_input)
                    st.markdown("**AI-Generated Advice:**")
                    st.success(ai_response)
            else:
                st.warning("Symptom database not available. Using AI response only.")
                ai_response = get_ai_response(user_input)
                st.success(ai_response)
                
        st.markdown("---\n*Remember: This is not medical advice. Always consult a professional Doctor for serious concerns.*")
    else:
        st.warning("Please enter your symptoms or question.")

st.markdown("### **Fitness Tracking: Calculate Your BMI**")
weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.1f")
height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")

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

st.caption("Stay safe and healthy! ✨")
