Agri-Bot: Your AI-Powered Agricultural Assistant
Agri-Bot is a comprehensive, multilingual web application built with Streamlit and powered by Google's Gemini AI. It's designed to provide farmers and agricultural professionals with instant access to expert knowledge, data-driven insights, and personalized advice.

This tool bridges the gap between advanced AI and practical farming needs, offering a suite of features from analyzing agricultural reports to providing crop-specific recommendations, all accessible through a simple and intuitive interface with voice input capabilities.

✨ Key Features
Prompt-Based Solutions: Ask any agriculture-related question in natural language and receive detailed, informative answers from the Gemini AI model. Supports both text and voice input.

PDF Report Analysis: Upload agricultural reports, research papers, or soil tests in PDF format to instantly summarize, identify key themes, or fact-check the content.

Crop-Specific Advice: Get tailored recommendations for specific crops by providing details like crop name, soil type, and region. The AI provides advice on best practices, soil management, and climate considerations.

Multilingual Support: Interact with the app in over 20 languages. Both input (text and voice) and output can be translated, making the tool accessible to a global audience.

Text-to-Speech (TTS): Have the AI's responses read out loud in your selected language for hands-free convenience.

🛠️ Tech Stack
Framework: Streamlit

AI Model: Google Gemini

Core Libraries:

google-generativeai for AI interactions

SpeechRecognition for voice-to-text

gTTS & google-cloud-translate for multilingual and TTS capabilities

PyMuPDF (fitz) for PDF text extraction

🚀 Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
Python 3.8 or higher

A Google API Key with the Gemini API enabled. You can obtain one from the Google AI Studio.

Installation & Setup
Clone the repository:

git clone https://github.com/Chiranthsgowda/aggribot.git
cd aggribot

Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Configure your environment variables:

Create a file named .env in the root directory of the project.

Add your Google API key to this file as shown below:

# .env file
GOOGLE_API_KEY="YOUR_SECRET_API_KEY_HERE"

The application uses this file for local development. This file is included in .gitignore and should never be committed to your repository.

▶️ How to Run the App
With your environment set up and dependencies installed, start the Streamlit application with the following command:

streamlit run Home.py

Your web browser should automatically open to the application's main page.

☁️ Deployment on Streamlit Community Cloud
This application is ready for deployment on Streamlit's free hosting platform.

Push to GitHub: Make sure your code, including the requirements.txt file, is pushed to your GitHub repository.

Create a Streamlit App:

Go to share.streamlit.io and click "New app".

Select your aggribot repository.

Add Your Secret Key:

Before deploying, go to the "Advanced settings..." section.

In the "Secrets" text area, add your Google API key in TOML format:

GOOGLE_API_KEY = "YOUR_SECRET_API_KEY_HERE"

Deploy: Click the "Deploy!" button. Streamlit will handle the rest!
