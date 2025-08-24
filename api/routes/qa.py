
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.services.qa_service import answer_question
from api.services.db_service import save_qa
from api.database import SessionLocal

router = APIRouter(prefix="/qa")

class QARequest(BaseModel):
    question: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")   # POST /qa
def get_answer(request: QARequest, db: Session = Depends(get_db)):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question must not be empty")

    # 1. Generate the answer from Gemini
    answer = answer_question(request.question)

    # 2. Save to DB
    saved = save_qa(db, question=request.question, answer=answer)

    # 3. Return full record
    return {
        "qa_id": saved.id,
        "question": saved.question,
        "answer": saved.answer,
        "asked_at": saved.asked_at.isoformat()
    }
