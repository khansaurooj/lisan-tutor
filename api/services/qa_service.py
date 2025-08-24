
from dotenv import load_dotenv
load_dotenv()  # 👈 this loads the .env file

import os
import google.generativeai as genai

# ✅ Now safe to access the environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("❌ GEMINI_API_KEY not found in environment")

genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def answer_question(question: str) -> str:
    try:
        response = model.generate_content(f"Answer this question precisely and concisely: {question}")
        return response.text.strip()
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return "Error generating answer."
