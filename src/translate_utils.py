import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
from googletrans import Translator

# Load .env
load_dotenv()

# Supported languages from config
SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "kn,en").split(",")
DEFAULT_TARGET_LANG = os.getenv("DEFAULT_TARGET_LANG", "en")

# Initialize translator
translator = Translator()


async def translate_text(text: str, target: str = DEFAULT_TARGET_LANG) -> str:
    """
    Translates text to the target language. Automatically detects source language.

    Args:
        text (str): Text to translate.
        target (str): Target language code.

    Returns:
        str: Translated text.
    """
    if not text.strip():
        return ""

    if target not in SUPPORTED_LANGUAGES:
        return f"Error: Unsupported target language. Supported languages: {', '.join(SUPPORTED_LANGUAGES)}"

    try:
        
        translation = await translator.translate(text, dest=target)
        return translation.text
    except Exception as e:
        return f"Error translating text: {str(e)}"
