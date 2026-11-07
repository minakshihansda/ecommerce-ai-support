from sqlalchemy.orm import Session

from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.product import Product
from app.db.models.user import User
from app.db.models.customer import Customer
from app.schemas.order_item import OrderItemCreate


def get_customer_by_user_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    return db.query(Customer).filter(
        Customer.email == user.email
    ).first()


def update_order_total(db: Session, order_id: int):
    items = db.query(OrderItem).filter(
        OrderItem.order_id == order_id
    ).all()

    total = sum(
        item.quantity * item.product.price
        for item in items
    )

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if order:
        order.total_amount = total


def create_order_item(
    db: Session,
    item_data: OrderItemCreate,
    user_id: int
):
    customer = get_customer_by_user_id(db, user_id)

    if not customer:
        raise ValueError("Customer profile not found")

    order = db.query(Order).filter(
        Order.id == item_data.order_id,
        Order.customer_id == customer.id
    ).first()

    if not order:
        raise ValueError("Order not found")

    if order.status != "Pending":
        raise ValueError("Products can only be added to Pending orders")

    product = db.query(Product).filter(
        Product.id == item_data.product_id
    ).first()

    if not product:
        raise ValueError("Product not found")

    if item_data.quantity < 1:
        raise ValueError("Quantity must be at least 1")

    try:
        # একই Product আগে থাকলে Quantity বাড়বে
        item = db.query(OrderItem).filter(
            OrderItem.order_id == order.id,
            OrderItem.product_id == product.id
        ).first()

        if item:
            item.quantity += item_data.quantity
        else:
            item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=item_data.quantity
            )
            db.add(item)

        db.flush()

        # Product-এর আসল দাম দিয়ে মোট দাম হিসাব
        update_order_total(db, order.id)

        db.commit()
        db.refresh(item)

        return item

    except Exception:
        db.rollback()
        raise


def get_order_item_by_id(db: Session, item_id: int):
    return db.query(OrderItem).filter(
        OrderItem.id == item_id
    ).first()