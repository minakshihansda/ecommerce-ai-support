from pydantic import BaseModel


class SupportTicketCreate(BaseModel):
    customer_id: int
    subject: str
    description: str


class SupportTicketResponse(BaseModel):
    id: int
    customer_id: int
    subject: str
    description: str
    status: str

    class Config:
        from_attributes = True