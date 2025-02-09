# AI Health Assistant

# Live Project Link
https://sympai.streamlit.app/

# Overview
  The AI Health Assistant is a Python-based application that provides health advice to users based on symptom detection. By leveraging machine learning models and natural language processing techniques, the assistant offers intelligent insights and symptom-based recommendations. This project was developed as part of the AICTE Internship on AI: Transformative Learning with TechSaksham, a joint CSR initiative by Microsoft and SAP.


# Key Features

**Symptom Detection:** Detects user symptoms and provides relevant health advice.
**Pretrained AI Model:** Utilizes cutting-edge machine learning models from the transformers library for natural language processing tasks.
**Efficient Data Handling:** Handles and processes health-related data efficiently using pandas and numpy.
**User-Friendly Interface:** Built with Streamlit for an interactive and intuitive user experience.
**Fuzzy Matching:** Integrates fuzzywuzzy for enhanced text matching capabilities.

# Project Structure
AI-Powered-Health-Assistant
├── app.py               # Main application entry point
├── health_data.csv       # Health-related dataset
├── models.py             # Pretrained model loading and handling
├── requirements.txt      # Project dependencies
├── symptom_processor.py  # Symptom processing logic
└── __pycache__/          # Cached files (excluded from version control)

# Technologies Used
   Programming Language: Python
  
**Frameworks and Libraries:**
   Streamlit: For building the web interface.
   transformers: Pretrained models for AI-driven health insights.
   torch: Deep learning framework for model execution.
   pandas: Data analysis and manipulation.
   numpy: Numerical computations.
   fuzzywuzzy and python-Levenshtein: For text-based fuzzy matching.

# Installation

**1. Clone the Repository**
   git clone https://github.com/M-Codes6/AI-Powered-Health-Assistant.git
   cd AI-Powered-Health-Assistant

**2. Set Up a Virtual Environment**
   python -m venv myenv
   source myenv/bin/activate   # On Windows, use myenv\Scripts\activate

**3. Install Dependencies**
   pip install -r requirements.txt

**4. Run the Application**
   streamlit run app.py

# Usage
   Open the Streamlit app in your browser.
   Enter your symptoms in the provided input field.
   Receive personalized health advice based on symptom detection.

# Project Highlights
   AI-Powered Insights: The use of pretrained models enables intelligent processing of user inputs.
   Data-Driven Recommendations: Health advice is supported by a comprehensive dataset.
   Fuzzy Matching: Accurate symptom detection even with user input variations.

# Acknowledgments
   This project was built as part of the AICTE Internship on AI: Transformative Learning with TechSaksham – a joint CSR initiative by Microsoft and SAP, focusing on AI 
   technologies.

# Future Enhancements
   Integration with additional health databases for broader symptom coverage.
   Improved user interface with more interactive features.
   Deployment as a cloud-based service.

# Contributing
  Contributions are welcome! Please follow these steps:

**Fork the repository.**
Create a new branch for your feature: git checkout -b feature/your-feature-name
Commit your changes: git commit -m "Add your feature description"
Push to your branch: git push origin feature/your-feature-name
Open a pull request.

# License
   This project is licensed under the MIT License.

# Contact
   For any inquiries, please reach out via GitHub Issues.
