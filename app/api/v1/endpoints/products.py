from fastapi import APIRouter

router = APIRouter()


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


@router.get("/products")
def products():
    return PRODUCTS


@router.get("/products/cheapest")
def cheapest_product():
    return min(PRODUCTS, key=lambda x: x["price"])


@router.get("/products/{product_id}")
def get_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}