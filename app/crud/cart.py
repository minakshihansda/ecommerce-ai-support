from sqlalchemy.orm import Session, joinedload

from app.db.models.cart_item import CartItem
from app.db.models.order import Order
from app.db.models.order_item import OrderItem
from app.db.models.product import Product
from app.db.models.customer import Customer
from app.db.models.user import User


def checkout_cart(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise ValueError("User not found")

    customer = db.query(Customer).filter(
        Customer.email == user.email
    ).first()

    if not customer:
        raise ValueError("Customer profile not found")

    try:
        cart_items = (
            db.query(CartItem)
            .options(joinedload(CartItem.product))
            .filter(CartItem.customer_id == customer.id)
            .all()
        )

        if not cart_items:
            raise ValueError("Your cart is empty")

        total_amount = 0

        for item in cart_items:
            if not item.product:
                raise ValueError("Product not found")

            total_amount += item.product.price * item.quantity

        order = Order(
            customer_id=customer.id,
            total_amount=total_amount,
            status="Pending",
            payment_status="Pending"
        )

        db.add(order)
        db.flush()

        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            db.add(order_item)

        for item in cart_items:
            db.delete(item)

        db.commit()
        db.refresh(order)

        return {
            "message": "Checkout successful",
            "order_id": order.id,
            "total_amount": order.total_amount,
            "status": order.status,
            "payment_status": order.payment_status
        }

    except Exception:
        db.rollback()
        raise