from sqlalchemy.orm import Session

from app.db.models.order_item import OrderItem
from app.schemas.order_item import OrderItemCreate


def create_order_item(db: Session, item_data: OrderItemCreate):
    item = OrderItem(
        order_id=item_data.order_id,
        product_id=item_data.product_id,
        quantity=item_data.quantity
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_order_item_by_id(db: Session, item_id: int):
    return (
        db.query(OrderItem)
        .filter(OrderItem.id == item_id)
        .first()
    )