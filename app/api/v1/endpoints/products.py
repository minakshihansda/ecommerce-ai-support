from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.product import Product

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/products")
def products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/products/cheapest")
def cheapest_product(db: Session = Depends(get_db)):
    return (
        db.query(Product)
        .order_by(Product.price.asc())
        .first()
    )


@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if product:
        return product

    return {"message": "Product not found"}