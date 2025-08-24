import os
import uuid
from moviepy.editor import VideoFileClip

def extract_audio(video_file_path: str) -> str:
    """
    Extracts audio from the given video file and saves it as MP3.
    Returns the path to the extracted audio file.
    """
    clip = VideoFileClip(video_file_path)
    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_output_path = os.path.join("static", "output", audio_filename)
    clip.audio.write_audiofile(audio_output_path)
    return audio_output_path

def save_temp_audio(uploaded_file) -> str:
    """
    Saves uploaded audio file to a temporary location and returns the path.
    """
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join("static", "output", filename)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.file.read())

    return file_path
