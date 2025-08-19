from translate_utils import translate_text
from tts_utils import text_to_speech_bytes
import streamlit as st
import speech_recognition as sr
from gemini_api import get_gemini_response
import asyncio
from pdf_utils import extract_text_from_pdf



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


# Language selection for voice input
language_option = st.selectbox("Select the language for voice input:", ["English", "Kannada", "Hindi", "Telugu", "Tamil", "Malayalam", "Bengali", "Gujarati", "Punjabi", "Marathi", "French", "German", "Spanish", "Chinese", "Russian", "Arabic", "Japanese", "Portuguese", "Thai", "Vietnamese"])
uploaded_file = st.file_uploader("Choose a report file (PDF only)")
if st.button("Extract Text"):
    # Extract text from the uploaded PDF file
    try:
        extracted_text = extract_text_from_pdf(uploaded_file)
        if extracted_text:
            st.session_state.extracted_text = extracted_text
            st.success("Text extracted successfully!")
        else:
            st.error("No text found in the PDF.")
    except Exception as e:
        st.error(f"Error extracting text: {str(e)}")

    st.write("Extracted Text:",extracted_text)

user_prompt = st.text_input("Enter your agriculture-related question or prompt here:", value="")
read = st.checkbox("Read the response aloud", value=True)

if st.button("Get Response"):
    prompt = "You are an expert in agriculture. " + user_prompt 
    response = get_gemini_response(prompt)
    
    
    if language_option != "English":
        response = asyncio.run(translate_text(response, language_codes[language_option]))


    st.subheader("Generated Response:")
    st.write(response)

    if read:
        audio_bytes = text_to_speech_bytes(response, language_codes[language_option])
        st.audio(audio_bytes, format="audio/wav")


if st.button("Voice Input"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
            with st.spinner('Listening...'):
                audio = recognizer.listen(source)  # Capture audio
        
            try:
            # Convert voice input to text (default is English)
                user_prompt1 = recognizer.recognize_google(audio, language='en-IN' if language_option == "English" else language_codes[language_option])
                st.success(f"Voice Input Captured: {user_prompt1}")
                st.session_state.user_prompt = user_prompt1
                # Process the voice input as needed


            except sr.UnknownValueError:
                st.error("Sorry, I could not understand your voice.")
            except sr.RequestError as e:
                st.error(f"Error with the voice recognition service: {e}")
 
if st.button("Get Response"):
    user_prompt = st.session_state.get('user_prompt', '')
    if not user_prompt:
        st.error("Please provide a question or prompt.")
    else:
        prompt = "You are an expert in agriculture. " + user_prompt 
        response = get_gemini_response(prompt)
        
        if language_option != "English":
            response = asyncio.run(translate_text(response, language_codes[language_option]))

        st.subheader("Generated Response:")
        st.write(response)