import os
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()

# API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Language settings
SUPPORTED_LANGUAGES = os.getenv("SUPPORTED_LANGUAGES", "kn,en").split(",")
DEFAULT_SOURCE_LANG = os.getenv("DEFAULT_SOURCE_LANG", "kn")
DEFAULT_TARGET_LANG = os.getenv("DEFAULT_TARGET_LANG", "en")
