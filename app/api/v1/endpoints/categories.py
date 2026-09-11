from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.crud.category import (
    create_category,
    get_all_categories,
    get_category_by_id,
    get_products_by_category,
)
from app.schemas.category import CategoryCreate, CategoryResponse


router = APIRouter()


@router.post("/categories", response_model=CategoryResponse)
def create_new_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    return create_category(db, category.name)


@router.get("/categories", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)


@router.get("/categories/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.get("/categories/{category_id}/products")
def products_by_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    products = get_products_by_category(db, category_id)

    if products is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return products