from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.chat import ChatRequest
from app.services.chat_service import get_ai_response

router = APIRouter()


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