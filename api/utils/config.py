from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TTS_LANG = os.getenv("TTS_LANG", "en")
