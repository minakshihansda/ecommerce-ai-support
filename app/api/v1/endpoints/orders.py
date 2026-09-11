from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.crud.order import create_order, get_order_by_id
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter()


@router.post("/orders", response_model=OrderResponse)
def create_new_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return create_order(db, order)


@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = get_order_by_id(db, order_id)

    if not order:
        return {"message": "Order not found"}

    return order