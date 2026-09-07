from sqlalchemy.orm import Session

from app.db.models.support_ticket import SupportTicket
from app.schemas.support_ticket import SupportTicketCreate


def create_support_ticket(
    db: Session,
    ticket_data: SupportTicketCreate
):
    ticket = SupportTicket(
        customer_id=ticket_data.customer_id,
        subject=ticket_data.subject,
        description=ticket_data.description
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_support_ticket_by_id(
    db: Session,
    ticket_id: int
):
    return (
        db.query(SupportTicket)
        .filter(SupportTicket.id == ticket_id)
        .first()
    )