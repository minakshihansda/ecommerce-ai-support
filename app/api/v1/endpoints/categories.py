from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.category import (
    create_category,
    get_all_categories,
    get_category_by_id,
)
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter()


@router.post("/categories", response_model=CategoryResponse)
def create_new_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
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
        return {"message": "Category not found"}

    return category