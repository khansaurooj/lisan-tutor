
### STEP 5: Full Video Pipeline
# D:\lisan-tutor\api\routes\video.py
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from api.services.video_service import process_video

router = APIRouter(prefix="/video")

@router.post("/")
async def video_pipeline(file: UploadFile = File(...), target_lang: str = Form(...)):
    result_video_path = await process_video(file, target_lang)
    return FileResponse(result_video_path, media_type="video/mp4", filename="translated_video.mp4")