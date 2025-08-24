from fastapi.responses import StreamingResponse
from fastapi import APIRouter, HTTPException, Form
from api.services.tts_service import text_to_speech

router = APIRouter(prefix="/tts")

@router.post("/")
async def tts_route(text: str = Form(...), lang: str = Form("en")):
    try:
        audio_path = text_to_speech(text, lang)

        def iterfile():
            with open(audio_path, mode="rb") as file_like:
                yield from file_like

        return StreamingResponse(iterfile(), media_type="audio/mpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
