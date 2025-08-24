
import tempfile
import whisper

model = whisper.load_model("base")

def transcribe_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return result["text"]