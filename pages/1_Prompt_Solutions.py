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

if st.button("Use Voice Input"):
    with sr.Microphone() as source:
        with st.spinner('Listening...'):
            audio = recognizer.listen(source)  # Capture audio
        
    try:
        # Convert voice input to text (default is English)
        user_prompt = recognizer.recognize_google(audio, language=STT_LANG_CODES.get(language_option, "en-IN"))
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
    prompt = "You are an expert in agriculture. " +  user_prompt + "keep the response very detailed and informative and clear and concise and in simple words."
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
