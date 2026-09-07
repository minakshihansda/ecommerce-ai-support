from sqlalchemy.orm import Session

from app.db.models.product import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


def get_cheapest_product(db: Session):
    return (
        db.query(Product)
        .order_by(Product.price.asc())
        .first()
    )