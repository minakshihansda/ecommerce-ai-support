from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.crud.product import (
    create_product,
    update_product,
    delete_product,
    get_all_products,
    get_cheapest_product,
    get_product_by_id,
)
from app.db.models.category import Category
from app.schemas.product import (
    ProductCategoryUpdate,
    ProductCreate,
    ProductUpdate,
)

router = APIRouter()


@router.post("/products")
def create_new_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return create_product(
        db,
        data.name,
        data.price
    )


@router.put("/products/{product_id}")
def update_product_details(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    product = update_product(
        db,
        product_id,
        data.name,
        data.price
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.delete("/products/{product_id}")
def delete_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    product = delete_product(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully",
        "id": product.id
    }


@router.get("/products")
def products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/products/cheapest")
def cheapest_product(db: Session = Depends(get_db)):
    return get_cheapest_product(db)


@router.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product_by_id(db, product_id)

    if product:
        return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@router.put("/products/{product_id}/category")
def update_product_category(
    product_id: int,
    data: ProductCategoryUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    category = (
        db.query(Category)
        .filter(Category.id == data.category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    product.category_id = data.category_id

    db.commit()
    db.refresh(product)

    return product