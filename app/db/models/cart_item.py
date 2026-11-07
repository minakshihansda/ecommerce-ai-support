from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(Integer, nullable=False, default=1)

    # একজন Customer একই Product একবারই Cart-এ রাখবে
    __table_args__ = (
        UniqueConstraint(
            "customer_id",
            "product_id",
            name="unique_customer_cart_product"
        ),
    )

    customer = relationship("Customer")
    product = relationship("Product")