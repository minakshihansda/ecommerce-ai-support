from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    total_amount = Column(Integer, nullable=False)

    status = Column(
        String(30),
        nullable=False,
        default="Pending"
    )

    payment_status = Column(
        String(30),
        nullable=False,
        default="Pending"
    )

    customer = relationship("Customer")

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )