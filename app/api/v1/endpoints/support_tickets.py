from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.support_ticket import (
    create_support_ticket,
    get_support_ticket_by_id,
)
from app.schemas.support_ticket import (
    SupportTicketCreate,
    SupportTicketResponse,
)

router = APIRouter()


@router.post(
    "/support-tickets",
    response_model=SupportTicketResponse
)
def create_new_support_ticket(
    ticket: SupportTicketCreate,
    db: Session = Depends(get_db)
):
    return create_support_ticket(db, ticket)


@router.get(
    "/support-tickets/{ticket_id}",
    response_model=SupportTicketResponse
)
def get_support_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = get_support_ticket_by_id(db, ticket_id)

    if not ticket:
        return {"message": "Support ticket not found"}

    return ticket