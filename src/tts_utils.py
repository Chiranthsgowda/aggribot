from gtts import gTTS
import io

def text_to_speech_bytes(text: str, lang: str = "en") -> bytes:
    """
    Convert text to speech and return raw audio bytes (MP3).
    No file is saved, only bytes are returned.

    Args:
        text (str): The input text to convert.
        lang (str): The language code ('en' for English, 'kn' for Kannada, etc.).

    Returns:
        bytes: MP3 audio data as raw bytes.
    """
    try:
        # Clean the text by removing asterisks
        cleaned_text = text.replace('*', '')

        # Create a gTTS object with the cleaned text and specified language
        tts = gTTS(text=cleaned_text, lang=lang)

        # Use an in-memory buffer to store the audio data
        audio_buffer = io.BytesIO()

        # Save the audio to the buffer instead of a file
        tts.write_to_fp(audio_buffer)

        # Move the buffer's cursor to the beginning
        audio_buffer.seek(0)

        return audio_buffer.read()  # raw audio bytes
    
    except Exception as e:
        raise RuntimeError(f"TTS Error: {str(e)}")
