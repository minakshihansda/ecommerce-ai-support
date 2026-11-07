from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.crud.order_item import (
    create_order_item,
    get_order_item_by_id,
    get_customer_by_user_id,
)
from app.db.models.order import Order
from app.schemas.order_item import (
    OrderItemCreate,
    OrderItemResponse,
)

router = APIRouter()


@router.post("/order-items", response_model=OrderItemResponse)
def create_new_order_item(
    item: OrderItemCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    try:
        return create_order_item(db, item, current_user_id)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/order-items/{item_id}",
    response_model=OrderItemResponse
)
def get_order_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    customer = get_customer_by_user_id(db, current_user_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer profile not found"
        )

    item = get_order_item_by_id(db, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    order = db.query(Order).filter(
        Order.id == item.order_id,
        Order.customer_id == customer.id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    return item