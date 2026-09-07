from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.db.models.product import Product


PRODUCTS = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 1499
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 2499
    },
    {
        "id": 3,
        "name": "USB-C Charger",
        "price": 799
    }
]


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        existing_products = db.query(Product).count()

        if existing_products == 0:
            for item in PRODUCTS:
                db.add(Product(**item))

            db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    init_db()