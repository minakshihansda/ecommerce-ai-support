from pydantic import BaseModel, ConfigDict, Field


class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int = Field(ge=1)


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class OrderProductDetails(BaseModel):
    product_id: int
    product_name: str
    price: int
    quantity: int


class OrderDetailsResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: int
    status: str
    payment_status: str
    items: list[OrderProductDetails]

    model_config = ConfigDict(from_attributes=True)