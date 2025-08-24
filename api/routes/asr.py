
from fastapi import APIRouter, UploadFile, File
from api.services.asr_service import transcribe_audio
from api.services.db_service import save_transcript

router = APIRouter()

@router.post("/asr/")
async def asr_endpoint(file: UploadFile = File(...)):
    # Transcribe the audio file
    transcript = transcribe_audio(file)
    
    # Save the transcript in the database and get the transcript_id
    transcript_id = save_transcript(original_text=transcript)
    
    # Return both transcript text and ID
    return {
        "transcription": transcript,
        "transcript_id": transcript_id
    }