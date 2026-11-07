from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user, get_current_admin

from app.crud.order import (
    create_order,
    get_order_by_user,
    get_order_details,
    get_orders_by_user,
    update_order_status,
    update_payment_status,
    track_order,
    cancel_order
)

from app.schemas.order import OrderCreate, OrderResponse
from app.schemas.order_item import OrderDetailsResponse

router = APIRouter()


# Create a new order
@router.post("/orders", response_model=OrderResponse)
def create_new_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    try:
        return create_order(db, order, current_user_id)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# Get customer's own order
@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    order = get_order_by_user(db, order_id, current_user_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# Admin: Get order details
@router.get(
    "/orders/{order_id}/details",
    response_model=OrderDetailsResponse
)
def get_order_details_api(
    order_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    order = get_order_details(db, order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "total_amount": order.total_amount,
        "status": order.status,
        "payment_status": order.payment_status,
        "items": [
            {
                "product_id": item.product_id,
                "product_name": item.product.name if item.product else "Unknown",
                "price": item.product.price if item.product else 0,
                "quantity": item.quantity
            }
            for item in order.items
        ]
    }


# Admin: Update order status
@router.put("/orders/{order_id}/status", response_model=OrderResponse)
def change_order_status(
    order_id: int,
    new_status: str,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    try:
        order = update_order_status(db, order_id, new_status)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# Admin: Update payment status
@router.put(
    "/orders/{order_id}/payment-status",
    response_model=OrderResponse
)
def change_payment_status(
    order_id: int,
    new_status: str,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    try:
        order = update_payment_status(db, order_id, new_status)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# Customer: Get all own orders
@router.get("/my-orders", response_model=list[OrderResponse])
def get_my_orders(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return get_orders_by_user(db, current_user_id)


# Customer: Get details of own order
@router.get(
    "/my-orders/{order_id}/details",
    response_model=OrderDetailsResponse
)
def get_my_order_details(
    order_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    order = get_order_by_user(db, order_id, current_user_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order = get_order_details(db, order_id)

    return {
        "id": order.id,
        "customer_id": order.customer_id,
        "total_amount": order.total_amount,
        "status": order.status,
        "payment_status": order.payment_status,
        "items": [
            {
                "product_id": item.product_id,
                "product_name": item.product.name if item.product else "Unknown",
                "price": item.product.price if item.product else 0,
                "quantity": item.quantity
            }
            for item in order.items
        ]
    }


# Customer: Track order
@router.get("/orders/{order_id}/track")
def order_tracking(
    order_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    order = track_order(db, order_id, current_user_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


# Customer: Cancel pending order
@router.put(
    "/orders/{order_id}/cancel",
    response_model=OrderResponse
)
def cancel_customer_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    order = cancel_order(db, order_id, current_user_id)

    if not order:
        raise HTTPException(
            status_code=400,
            detail="Order cannot be cancelled"
        )

    return order