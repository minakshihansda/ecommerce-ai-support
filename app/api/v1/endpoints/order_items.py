from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.order_item import (
    create_order_item,
    get_order_item_by_id,
)
from app.schemas.order_item import (
    OrderItemCreate,
    OrderItemResponse,
)

router = APIRouter()


@router.post("/order-items", response_model=OrderItemResponse)
def create_new_order_item(
    item: OrderItemCreate,
    db: Session = Depends(get_db)
):
    return create_order_item(db, item)


@router.get("/order-items/{item_id}", response_model=OrderItemResponse)
def get_order_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = get_order_item_by_id(db, item_id)

    if not item:
        return {"message": "Order item not found"}

    return item