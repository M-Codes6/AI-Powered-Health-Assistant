import streamlit as st

st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="🧳")

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

        /* Center container for button and spinner */
        .center-button {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        /* Button Styling */
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

        /* Remove text decoration for links */
        .custom-button:link, 
        .custom-button:visited {
            text-decoration: none;
            color: #fff;
        }

        /* Spinner Styling */
        .loader {
            border: 4px solid #f3f3f3; /* Light grey */
            border-top: 4px solid #f56a79; /* Custom color */
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
            margin-bottom: 5px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
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
st.markdown('<p class="app-description">Your trusted companion for health advice, fitness tips, and personalized recommendations powered by AI. Stay healthy, stay informed!</p>', unsafe_allow_html=True)


st.markdown("""
    <div class="center-button">
        <a href="https://sympai.streamlit.app/main" class="custom-button" id="getStartedBtn" onclick="document.getElementById('spinnerDiv').style.display='block'">
            Get Started
        </a>
        <div id="spinnerDiv" style="display: none; margin-top: 10px; text-align: center;">
            <div class="loader"></div>
            <p>Hold on, we are loading page for you</p>
        </div>
    </div>
""", unsafe_allow_html=True)
