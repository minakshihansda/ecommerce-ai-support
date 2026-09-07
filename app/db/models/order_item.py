from sqlalchemy import Column, Integer, ForeignKey

from app.db.base import Base
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.db.models.product import Product
from app.db.models.customer import Customer
from app.db.models.order import Order
from app.db.models.order_item import OrderItem

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)