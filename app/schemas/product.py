from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: int


class ProductUpdate(BaseModel):
    name: str
    price: int


class ProductCategoryUpdate(BaseModel):
    category_id: int