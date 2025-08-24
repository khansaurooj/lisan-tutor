
# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from api.services.translation_service import translate_text_pipeline

# router = APIRouter()

# class TranslationRequest(BaseModel):
#     text: str
#     src_lang: str
#     tgt_lang: str

# @router.post("/translate/")
# async def translate_endpoint(req: TranslationRequest):
#     try:
#         translated = translate_text_pipeline(req.text, req.src_lang, req.tgt_lang)
#         return {
#             "original_text": req.text,
#             "translated_text": translated
#         }
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Translation failed: " + str(e))




from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.translation_service import translate_text_pipeline

router = APIRouter(prefix="/translate", tags=["translation"])

class TranslationRequest(BaseModel):
    text: str
    src_lang: str
    tgt_lang: str

@router.post("/", summary="Translate text from one language to another")
async def translate_endpoint(req: TranslationRequest):
    """
    POST /translate/
    Body JSON:
      {
        "text": "...",
        "src_lang": "en",
        "tgt_lang": "ur"
      }
    Returns JSON:
      {
        "original_text": "...",
        "translated_text": "..."
      }
    """
    try:
        translated = translate_text_pipeline(req.text, req.src_lang, req.tgt_lang)
        return {
            "original_text": req.text,
            "translated_text": translated
        }
    except ValueError as e:
        # invalid language pair, etc.
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # any other error
        raise HTTPException(status_code=500, detail="Translation failed: " + str(e))
