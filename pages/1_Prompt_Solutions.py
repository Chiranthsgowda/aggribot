import streamlit as st
import speech_recognition as sr
from src.translate_utils import translate_text
from src.gemini_api import get_gemini_response
from src.tts_utils import text_to_speech_bytes
import asyncio

# Initialize the speech recognizer
recognizer = sr.Recognizer()

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #3CB371, #2E8B57, #1E90FF);
    }
    </style>
    """,
    unsafe_allow_html=True
) #Set the background color of the app

st.header("Prompt-Based Solutions")

selected_question = ""

# List of suggested questions
suggested_questions = [
       "What crops are best suited for the upcoming season?",
    "What recent data is available on how climate change is impacting crop yields across different regions? How can I use this information to plan my next planting season?",
    "What strategies can I adopt for conserving water on my farm, and can you provide data on the most effective water-saving techniques in semi-arid areas?",
    "What are some organic soil amendments I can use to improve soil health, and do you have data on their effectiveness for long-term fertility?",
    "Which fertilizers are recommended for wheat to maximize yield, and could you provide any recent data on their effectiveness?",
    "Can you share the latest global trends in sustainable farming practices that could be adopted to make farming environmentally friendly?",
    "I'm facing pest issues in my rice fields. Can you recommend some organic pest control methods, along with any data on their effectiveness and usage guidelines?",
    "Can you explain the benefits of crop rotation and share recent studies or data showing its impact on reducing pests and improving soil structure?",

    ]

selected_question = st.selectbox("Suggested Questions", [""] + suggested_questions)

    
language_codes = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh",
    "Russian": "ru",
    "Arabic": "ar",
    "Japanese": "ja",
    "Portuguese": "pt",
    "Thai": "th",
    "Vietnamese": "vi"
}

STT_LANG_CODES = { "English": "en-IN", "Kannada": "kn-IN", "Hindi": "hi-IN", "Telugu": "te-IN", "Tamil": "ta-IN", "Malayalam": "ml-IN", "Bengali": "bn-IN", "Gujarati": "gu-IN", "Punjabi": "pa-IN", "Marathi": "mr-IN", "French": "fr-FR", "German": "de-DE", "Spanish": "es-ES", "Chinese": "zh-CN", "Russian": "ru-RU", "Arabic": "ar-SA", "Japanese": "ja-JP", "Portuguese": "pt-PT", "Thai": "th-TH", "Vietnamese": "vi-VN" }


# Language selection for voice input
language_option = st.selectbox("Select the language for voice input and Response:", ["English", "Kannada", "Hindi", "Telugu", "Tamil", "Malayalam", "Bengali", "Gujarati", "Punjabi", "Marathi", "French", "German", "Spanish", "Chinese", "Russian", "Arabic", "Japanese", "Portuguese", "Thai", "Vietnamese"])

if 'user_prompt' not in st.session_state:
    st.session_state.user_prompt = ""  

import sounddevice as sd
import numpy as np

if st.button("Use Voice Input"):
    with st.spinner("Listening..."):
        duration = 5  # seconds
        sample_rate = 44100

        # Record from microphone
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()

        # Convert numpy array to AudioData for speech_recognition
        audio_data = sr.AudioData(recording.tobytes(), sample_rate, 2)

        try:
            # Speech recognition
            user_prompt = recognizer.recognize_google(audio_data, language=STT_LANG_CODES.get(language_option, "en-IN"))
            st.success(f"Voice Input Captured: {user_prompt}")
            
        # If the language is not in English, translate it to English
            if language_option != "English":
                translation = asyncio.run(translate_text(user_prompt))
                user_prompt = translation  # Update the user prompt with the English translation
                st.success(f"Translated to English: {user_prompt}")

            st.session_state.user_prompt = user_prompt

        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your voice.")
        except sr.RequestError as e:
            st.error(f"Error with the voice recognition service: {e}")
    
if st.session_state.user_prompt == "":
    default_value = selected_question

else:
    default_value = st.session_state.user_prompt

user_prompt = st.text_input("Enter your agriculture-related question or prompt here:", value=default_value)

read = st.checkbox("read out the response")


# Generate response button
if st.button("Get Response"):
    prompt = prompt = "Act as a world-class agricultural expert, capable of adapting your role to be a scientist, extension officer, or plant pathologist as needed. Your primary goal is to provide the most helpful, clear, and practical response for a non-expert.\n\nFirst, analyze the user's query to determine its type:\n1. Is it a General Information question (e.g., \"What is drip irrigation?\")?\n2. Is it a Procedural \"How-To\" question (e.g., \"How do I make compost?\")?\n3. Is it a Problem-Solving/Diagnostic question (e.g., \"Why are my crops wilting?\")?\n\nBased on your analysis, you must use the corresponding structure below to formulate your answer.\n\n---\n\nStructure for General Information Queries:\n1. Executive Summary: Begin with a 2-3 sentence direct answer.\n2. Detailed Explanation: Break down the topic with clear headings and bullet points. Explain complex terms simply.\n3. Key Takeaways & Practical Applications: Conclude with the most important points and how the information can be used in practice.\n\n---\n\nStructure for Procedural \"How-To\" Queries:\n1. Objective & Prerequisites: State the goal and list all necessary tools, materials, or conditions.\n2. Step-by-Step Guide: Provide clear, numbered steps for the process. Each step should be a single, actionable task.\n3. Tips for Success & Common Pitfalls: Offer expert advice for getting the best results and avoiding common mistakes.\n\n---\n\nStructure for Problem-Solving/Diagnostic Queries:\n1. Most Likely Causes: List the top potential causes, from most to least probable.\n2. Diagnosis & Confirmation: For each cause, explain how to confirm it (e.g., \"Look for X on the underside of the leaf.\").\n3. Actionable Solutions: Provide clear solutions for each cause, separated into (a) Immediate Fixes and (b) Long-Term Prevention.\n\n---\n\nUniversal Rule: Regardless of the query type, your entire response must use simple, easy-to-understand language. Be comprehensive yet concise.\n\nHere is the query: "+  user_prompt + "Don't mention anything about yourself and query type just start with answering the query directly"
    response = get_gemini_response(prompt)

    if language_option != "English":
        response = asyncio.run(translate_text(response,language_codes[language_option]))

    st.subheader("Generated Response:")
    st.write(response)

    # Read out the response
    if read:
        st.write("This will take time based on the length of the response.It may take a few seconds to generate the speech.")
        try:
            # Store the returned bytes directly in a clearly named variable.
            audio_bytes = text_to_speech_bytes(response, lang=language_codes[language_option])
                
            # 3. Pass these bytes DIRECTLY to st.audio. No need to open a file.
            st.audio(audio_bytes, format="audio/mp3")
                
            st.success(f"Speech generated in {language_option}!")
            st.write("Thank you for your patience.🥰")

        except Exception as e:
            st.error(f"An error occurred while generating speech: {e}")
        
    if response != "":
        st.session_state.user_prompt = ""
        selected_question = ""
        user_prompt = ""
