# D:\lisan-tutor\api\services\tts_service.py
from gtts import gTTS
import os
import uuid

def text_to_speech(text, lang="en"):
    if not text.strip():
        raise ValueError("TTS received empty text")

    supported_langs = ["en", "ur", "fr", "es"]  # add more as needed
    if lang not in supported_langs:
        lang = "en"  # fallback to English

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join("static", "output", filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(filepath)
    return filepath
