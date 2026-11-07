from pydantic import BaseModel, ConfigDict, Field


class OrderCreate(BaseModel):
    total_amount: int = Field(gt=0)


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: int
    status: str
    payment_status: str

    model_config = ConfigDict(from_attributes=True)