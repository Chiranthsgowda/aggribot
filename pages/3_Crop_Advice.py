import streamlit as st
from src.gemini_api import get_gemini_response
from src.tts_utils import text_to_speech_bytes
from src.translate_utils import translate_text
import asyncio

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

# Set the header for the page
st.header("Crop-Specific Advice")

# Input fields for crop advice
st.subheader("Enter Crop Details")
crop_name = st.text_input("Crop Name")
soil_type = st.text_input("Soil Type")
region = st.text_input("Region")

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

language_option = st.selectbox("Select the language for voice input:", ["English", "Kannada", "Hindi", "Telugu", "Tamil", "Malayalam", "Bengali", "Gujarati", "Punjabi", "Marathi", "French", "German", "Spanish", "Chinese", "Russian", "Arabic", "Japanese", "Portuguese", "Thai", "Vietnamese"])


read = st.checkbox("read out the response")

# Crop advice button
if st.button("Get Crop Advice"):
        if crop_name and soil_type and region:
            crop_prompt = (
                f"You are an agriculture expert. Provide advice for '{crop_name}' in '{soil_type}' soil in '{region}'. "
                "Include best practices, soil management, and climate considerations. "
                "Begin with a general suitability rating for the crop in this setup."
                "Don't mention anything about yourself and just start with answering the query directly"
            )

            response = get_gemini_response(crop_prompt)

            # Translate response if the selected language is not English
            if language_option != "English":
                response = asyncio.run(translate_text(response, language_codes[language_option]))

            st.subheader("Crop-Specific Advice:")
            st.write(response)

            # Read out the response
            if read:
                st.write("This will take time based on the length of the response.It may take a few seconds to generate the speech.")
                try:
                    # Store the returned bytes directly in a clearly named variable.
                    audio_bytes = text_to_speech_bytes(response, lang=language_codes[language_option])
                
                    # Pass these bytes DIRECTLY to st.audio. No need to open a file.
                    st.audio(audio_bytes, format="audio/mp3")
                
                    st.success(f"Speech generated in {language_option}!")
                    st.write("Thank you for your patience.🥰")

                except Exception as e:
                    st.error(f"An error occurred while generating speech: {e}")
