from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id: int
    total_amount: int


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: int

    class Config:
        from_attributes = True