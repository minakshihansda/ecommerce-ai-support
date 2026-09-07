from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.chat import ChatRequest
from app.services.chat_service import get_ai_response

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    try:
        answer = get_ai_response(request.message, db)

        return {
            "answer": answer
        }

    except Exception:
        return {
            "error": "Sorry, the AI service is temporarily unavailable."
        }