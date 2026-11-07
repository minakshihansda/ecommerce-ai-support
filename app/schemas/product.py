from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    price: int
    image_url: Optional[str] = None


class ProductUpdate(BaseModel):
    name: str
    price: int
    image_url: Optional[str] = None


class ProductCategoryUpdate(BaseModel):
    category_id: int