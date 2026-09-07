from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import get_ai_response

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    try:
        answer = get_ai_response(request.message)

        return {
            "answer": answer
        }

    except Exception:
        return {
            "error": "Sorry, the AI service is temporarily unavailable."
        }