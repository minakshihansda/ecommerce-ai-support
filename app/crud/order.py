from sqlalchemy.orm import Session, joinedload

from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.customer import Customer
from app.db.models.user import User
from app.schemas.order import OrderCreate


ORDER_STATUSES = {
    "Pending", "Confirmed", "Processing", "Shipped",
    "Out for Delivery", "Delivered", "Cancelled", "Returned"
}

PAYMENT_STATUSES = {
    "Pending", "Paid", "Failed", "Refunded"
}


def get_customer_by_user_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    return db.query(Customer).filter(
        Customer.email == user.email
    ).first()


def create_order(db: Session, order_data: OrderCreate, user_id: int):
    customer = get_customer_by_user_id(db, user_id)

    if not customer:
        raise ValueError("Customer profile not found for this user")

    order = Order(
        customer_id=customer.id,
        total_amount=order_data.total_amount,
        status="Pending",
        payment_status="Pending"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(
        Order.id == order_id
    ).first()


def get_order_by_user(db: Session, order_id: int, user_id: int):
    customer = get_customer_by_user_id(db, user_id)

    if not customer:
        return None

    return db.query(Order).filter(
        Order.id == order_id,
        Order.customer_id == customer.id
    ).first()


def get_order_details(db: Session, order_id: int):
    return (
        db.query(Order)
        .options(
            joinedload(Order.items).joinedload(OrderItem.product)
        )
        .filter(Order.id == order_id)
        .first()
    )


def get_orders_by_user(db: Session, user_id: int):
    customer = get_customer_by_user_id(db, user_id)

    if not customer:
        return []

    return db.query(Order).filter(
        Order.customer_id == customer.id
    ).order_by(Order.id.desc()).all()


def update_order_status(db: Session, order_id: int, new_status: str):
    if new_status not in ORDER_STATUSES:
        raise ValueError("Invalid order status")

    order = get_order_by_id(db, order_id)

    if not order:
        return None

    order.status = new_status
    db.commit()
    db.refresh(order)

    return order


def update_payment_status(db: Session, order_id: int, new_status: str):
    if new_status not in PAYMENT_STATUSES:
        raise ValueError("Invalid payment status")

    order = get_order_by_id(db, order_id)

    if not order:
        return None

    order.payment_status = new_status
    db.commit()
    db.refresh(order)

    return order


def track_order(db: Session, order_id: int, user_id: int):
    order = get_order_by_user(db, order_id, user_id)

    if not order:
        return None

    return {
        "order_id": order.id,
        "status": order.status,
        "payment_status": order.payment_status,
        "total_amount": order.total_amount
    }


def cancel_order(db: Session, order_id: int, user_id: int):
    order = get_order_by_user(db, order_id, user_id)

    if not order or order.status != "Pending":
        return None

    order.status = "Cancelled"
    db.commit()
    db.refresh(order)

    return order