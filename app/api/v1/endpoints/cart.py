from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel, Field

from app.api.deps import get_db, get_current_user
from app.crud.order import get_customer_by_user_id
from app.db.models.cart_item import CartItem
from app.db.models.product import Product
from app.crud.cart import checkout_cart

router = APIRouter()


class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)


def get_cart_items(db: Session, customer_id: int):
    return (
        db.query(CartItem)
        .options(joinedload(CartItem.product))
        .filter(CartItem.customer_id == customer_id)
        .all()
    )


@router.get("/cart")
def view_cart(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    customer = get_customer_by_user_id(db, current_user_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer profile not found")

    items = get_cart_items(db, customer.id)

    cart = []
    total = 0

    for item in items:
        subtotal = item.product.price * item.quantity
        total += subtotal

        cart.append({
            "id": item.id,
            "product_id": item.product_id,
            "product_name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    return {
        "items": cart,
        "total_items": sum(item.quantity for item in items),
        "total_amount": total
    }


@router.post("/cart/items")
def add_to_cart(
    data: CartItemCreate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    customer = get_customer_by_user_id(db, current_user_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer profile not found")

    product = db.query(Product).filter(
        Product.id == data.product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    try:
        item = db.query(CartItem).filter(
            CartItem.customer_id == customer.id,
            CartItem.product_id == data.product_id
        ).first()

        if item:
            item.quantity += data.quantity
        else:
            item = CartItem(
                customer_id=customer.id,
                product_id=data.product_id,
                quantity=data.quantity
            )
            db.add(item)

        db.commit()
        db.refresh(item)

        return {
            "message": "Product added to cart",
            "product_id": item.product_id,
            "quantity": item.quantity
        }

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not add product to cart")


@router.put("/cart/items/{product_id}")
def update_cart_item(
    product_id: int,
    data: CartItemUpdate,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    customer = get_customer_by_user_id(db, current_user_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer profile not found")

    item = db.query(CartItem).filter(
        CartItem.customer_id == customer.id,
        CartItem.product_id == product_id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = data.quantity
    db.commit()

    return {"message": "Cart quantity updated"}


@router.delete("/cart/items/{product_id}")
def remove_cart_item(
    product_id: int,
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    customer = get_customer_by_user_id(db, current_user_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer profile not found")

    item = db.query(CartItem).filter(
        CartItem.customer_id == customer.id,
        CartItem.product_id == product_id
    ).first()

    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    db.delete(item)
    db.commit()

    return {"message": "Product removed from cart"}
@router.post("/cart/checkout")
def checkout(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_current_user)
):
    try:
        return checkout_cart(db, current_user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))