from sqlalchemy.orm import Session

from app.db.models.order import Order
from app.schemas.order import OrderCreate


def create_order(db: Session, order_data: OrderCreate):
    order = Order(
        customer_id=order_data.customer_id,
        total_amount=order_data.total_amount
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_order_by_id(db: Session, order_id: int):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )