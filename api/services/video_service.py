
# D:\lisan-tutor\api\services\video_service.py
import uuid
import moviepy.editor as mp
from api.services.asr_service import transcribe_audio
from api.services.translation_service import translate_text_pipeline
from api.services.tts_service import text_to_speech
from fastapi import UploadFile

async def process_video(file: UploadFile, target_lang: str) -> str:
    input_video_path = f"static/{uuid.uuid4()}.mp4"
    with open(input_video_path, "wb") as f:
        f.write(await file.read())

    video = mp.VideoFileClip(input_video_path)
    audio_path = input_video_path.replace(".mp4", ".mp3")
    video.audio.write_audiofile(audio_path)

    with open(audio_path, "rb") as audio_file:
        class DummyFile:
            file = audio_file
        original_text = transcribe_audio(DummyFile())

    translated_text = translate_text_pipeline(original_text, src_lang="en", tgt_lang=target_lang)

    tts_audio_path = text_to_speech(translated_text, lang=target_lang)

    final_output_path = input_video_path.replace(".mp4", "_final.mp4")
    new_audio = mp.AudioFileClip(tts_audio_path)
    video = video.set_audio(new_audio)
    video.write_videofile(final_output_path, codec="libx264", audio_codec="aac")

    return final_output_path
