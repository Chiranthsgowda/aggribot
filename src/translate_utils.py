import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
import asyncio

# Load .env
load_dotenv()

# Supported languages from config
SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "kn,en").split(",")
DEFAULT_TARGET_LANG = os.getenv("DEFAULT_TARGET_LANG", "en")


async def translate_text(text: str, target: str = DEFAULT_TARGET_LANG, max_retries: int = 3) -> str:
    """
    Translates text to the target language using deep-translator.

    Args:
        text (str): Text to translate.
        target (str): Target language code.
        max_retries (int): Maximum number of retry attempts.

    Returns:
        str: Translated text or original text if translation fails.
    """
    if not text.strip():
        return ""

    # Skip translation if target is English and text appears to be English
    if target == "en":
        # Simple heuristic: if text contains mostly ASCII characters, likely English
        ascii_ratio = sum(1 for c in text if ord(c) < 128) / len(text)
        if ascii_ratio > 0.8:
            return text

    if target not in SUPPORTED_LANGUAGES:
        return f"Error: Unsupported target language. Supported languages: {', '.join(SUPPORTED_LANGUAGES)}"

    for attempt in range(max_retries):
        try:
            # Add delay between retries
            if attempt > 0:
                await asyncio.sleep(2 ** attempt)
            
            # Use deep-translator which is more reliable
            translator = GoogleTranslator(source='auto', target=target)
            translated_text = translator.translate(text)
            
            if translated_text:
                return translated_text
            else:
                raise Exception("Translation returned empty result")
                
        except Exception as e:
            print(f"Translation attempt {attempt + 1} failed: {str(e)}")
            
            # On last attempt, return original text
            if attempt == max_retries - 1:
                print(f"All translation attempts failed. Returning original text.")
                return text
    
    # Fallback
    return text


# Backup function using googletrans (if deep-translator fails)
async def translate_text_backup(text: str, target: str = DEFAULT_TARGET_LANG) -> str:
    """
    Backup translation function using googletrans.
    """
    try:
        from googletrans import Translator
        translator = Translator(timeout=10)
        
        translation = translator.translate(text, dest=target)
        if translation and translation.text:
            return translation.text
    except Exception as e:
        print(f"Backup translation failed: {str(e)}")
    
    return text  # Return original text if all else fails


# Main function that tries deep-translator first, then falls back
async def robust_translate_text(text: str, target: str = DEFAULT_TARGET_LANG) -> str:
    """
    Robust translation that tries multiple methods.
    """
    # Try deep-translator first
    result = await translate_text(text, target)
    
    # If deep-translator failed (returned original text), try backup
    if result == text and target != "en":
        result = await translate_text_backup(text, target)
    
    return result
