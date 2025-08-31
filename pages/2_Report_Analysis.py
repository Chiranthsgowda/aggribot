import streamlit as st
from src.pdf_utils import extract_text_from_pdf
from src.tts_utils import text_to_speech_bytes
from src.gemini_api import get_gemini_response
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
) # Set the background color of the app


st.header("Report Analysis")

# Upload PDF file
uploaded_file = st.file_uploader("Choose a report file (PDF only)")

# Select analysis task
task = st.selectbox("Select analysis task", ["Summarize", "Identify Themes", "Fact-Check"])

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

# Analysis button
if st.button("Analyze"):
    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
        prompt = f"Act as a world-class agricultural expert, capable of adapting your role to be a scientist, extension officer, or plant pathologist as needed. Your primary goal is to provide the most helpful, clear, and practical response for a non-expert.Analyze the following report for {task}:\n\n{text}.Don't mention anything about yourself and just start with answering the query directly"
        response = get_gemini_response(prompt)
        
        if language_option!= "English":
            response = asyncio.run(translate_text(response, language_codes[language_option]))
        
        st.subheader("Analysis Result:")
        st.write(response)

        # Read out the response
        if read:
            try:
                st.write("This will take time based on the length of the response.It may take a few seconds to generate the speech.")
                # Store the returned bytes directly in a clearly named variable.
                audio_bytes = text_to_speech_bytes(response, lang=language_codes[language_option])
                
                # 3. Pass these bytes DIRECTLY to st.audio. No need to open a file.
                st.audio(audio_bytes, format="audio/mp3")
                
                st.success(f"Speech generated in {language_option}!")
                st.write("Thank you for your patience.🥰")

            except Exception as e:
                st.error(f"An error occurred while generating speech: {e}")
