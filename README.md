# Lisan-Khansa
## Lisan Tutor — AI Tutor for Every Tongue
Lisan Tutor is an intelligent, multilingual AI tutor built with FastAPI and integrated with advanced models for Automatic Speech Recognition (ASR), Translation, Text-to-Speech (TTS), and Question Answering (QA).

🎯 Designed to help users:

- Transcribe audio in any language using Whisper  
- Translate the text into a target language using Hugging Face models  
- Speak the translated text aloud using TTS  

---

### ✨ Features

- 🎙️ **Speech-to-Text (ASR)** – Convert audio input into written text using OpenAI Whisper.  
- 🌍 **Translation** – Translate transcribed text into over 100 languages using Hugging Face models.  
- 🔊 **Text-to-Speech (TTS)** – Listen to translated text with voice generation powered by Coqui TTS.  
- ❓ **Question Answering** – Ask questions from the transcribed + translated content.  
- 📼 **Video Support** – Upload or record videos and get full educational content in your preferred language.  
- 🌐 **Frontend UI** – User-friendly interface built with HTML, CSS, and JavaScript.  
- ⚡ **FastAPI Backend** – Handles audio upload, processing, and model inference.  

---

### 🔧 Technologies Used

| Layer          | Tools & Libraries |
|----------------|-------------------|
| Backend        | FastAPI, Python, Whisper, Transformers (Hugging Face), Coqui TTS |
| Frontend       | HTML, CSS, JavaScript |
| AI Models      | OpenAI Whisper, MarianMT, BERT, TTS (Coqui) |
| Miscellaneous  | ffmpeg, Git, GitHub |

---

### 📂 Project Structure

```
project_root/
│
├── api/                         # Main API logic
│   ├── routes/                  # Route handlers (FastAPI endpoints)
│   │   ├── init.py
│   │   ├── asr.py
│   │   ├── qa.py
│   │   ├── translation.py
│   │   ├── tts.py
│   │   ├── video.py
│   │
│   ├── services/                # Business logic
│   │   ├── init.py
│   │   ├── asr_service.py
│   │   ├── qa_service.py
│   │   ├── translation_service.py
│   │   ├── tts_service.py
│   │   ├── video_service.py
│   │
│   ├── utils/                   # Utility/helper functions
│   │   ├── init.py
│   │   ├── audio_utils.py
│   │   ├── video_utils.py
│   │   ├── config.py            # Configuration settings (e.g. env vars, constants)
│   │
│   └── main.py                  # FastAPI entry point
│
├── frontend/                    # Frontend app (HTML/JS/CSS)
│   ├── app.js
│   ├── index.html
│   └── styles.css
│
├── sample_data/                # Sample input files (for development/testing)
│   ├── sample_audio.opus
│   └── sample_video.mp4
│
├── static/                      # Static assets (e.g. result/output files)
│   └── output/
│
├── tests/                       # Unit and integration tests
│   ├── test_asr.py
│   ├── test_qa.py
│   ├── test_translation.py
│   ├── test_tts.py
│   └── test_video.py
│
├── venv/                        # Python virtual environment (should be in .gitignore)
│
├── requirements.txt             # Python dependencies
│
└── README.md                    # Optional: here you are
```

---

### ⚙️ Setup Instructions

**Clone the Repo:**

```bash
git clone https://github.com/your-username/ai-tutor-for-every-tongue.git
cd ai-tutor-for-every-tongue
```

**Create Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Install ffmpeg (Required for audio/video processing)**  
Download and add to PATH from: https://ffmpeg.org/download.html

**Run the Server:**

```bash
uvicorn main:app --reload
```

**Open Frontend:**  
Navigate to: http://localhost:8000  
Use the interface to upload audio/video and interact with your AI tutor!

---

### ▶️ How to Use

- 🎥 Upload or Record Video/Audio  
- 🧠 Transcribe with Whisper  
- 🌐 Translate to Desired Language  
- 🔊 Generate Audio from Translation  
- ❓ Ask Questions and Get Answers  
- 📄 View/download processed text or audio  

---

### 📑 Word Documentation

See [Google Docs](https://docs.google.com/document/d/1v4uU9bbT_kiszUalTRp7J8TFhqryBJGJ/edit?usp=drive_link&ouid=101868376929908463596&rtpof=true&sd=true) for a complete walkthrough of how the system works, model architecture, and how to contribute.

---

### 🔮 To-Do / Future Improvements

- Add language auto-detection  
- Add speaker diarization  

---

### 👥 Contributors

👩‍💻 **Khansa Urooj** – Software Engineer @ FJWU 🎓 [GitHub](https://github.com/khansaurooj)

---

### 📜 License

This project is licensed under the **MIT License**.

---
