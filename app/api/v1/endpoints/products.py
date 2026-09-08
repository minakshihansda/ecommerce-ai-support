from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.product import (
    get_all_products,
    get_cheapest_product,
    get_product_by_id,
)

router = APIRouter()


@router.get("/products")
def products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/products/cheapest")
def cheapest_product(db: Session = Depends(get_db)):
    return get_cheapest_product(db)


@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)

    if product:
        return product

    return {"message": "Product not found"}
@app.get("/products")