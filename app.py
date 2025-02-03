import streamlit as st

st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="🧳")

# CSS Styling with Animations
st.markdown("""
    <style>
        /* Hide the entire toolbar containing Share, GitHub, etc. */
        .stToolbarActions { 
            display: none !important; 
        }
            
        h1 {
            text-align: center;
            font-size: 1.2rem;
            opacity: 0.6;
            animation: fadeIn 3s ease-in-out;
        }

        p.app-description {
            font-size: 1.1rem;
            text-align: center;
            animation: slideIn 2s ease-in-out;
            color: #555;
        }

        /* Button Styling */
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .custom-button {
            background-color: #f56a79;
            color: white;
            padding: 0.6rem 1.5rem;
            border-radius: 1rem;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            text-align: center;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.15);
            transition: all 0.3s ease-in-out;
        }

        .custom-button:hover {
            background-color: #f5425d;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)


st.title("🧳 Welcome to AI-Powered Health Assistant")

# App description
st.markdown('<p class="app-description">Your trusted companion for health advice, fitness tips, and personalized recommendations powered by AI. Stay healthy, stay informed!</p>', unsafe_allow_html=True)

# Centered Get Started Button with Navigation Link
st.markdown("""
    <div class="center-button">
        <a href="https://sympai.streamlit.app/main" class="custom-button">Get Started</a>
    </div>
""", unsafe_allow_html=True)
