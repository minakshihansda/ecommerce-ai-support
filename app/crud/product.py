from sqlalchemy.orm import Session, joinedload

from app.db.models.product import Product


def create_product(
    db: Session,
    name: str,
    price: int,
    image_url: str = None
):
    product = Product(
        name=name,
        price=price,
        image_url=image_url
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def update_product(
    db: Session,
    product_id: int,
    name: str,
    price: int,
    image_url: str = None
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        return None

    product.name = name
    product.price = price
    product.image_url = image_url

    db.commit()
    db.refresh(product)

    return product


def get_all_products(db: Session):
    return (
        db.query(Product)
        .options(joinedload(Product.category))
        .all()
    )


def get_product_by_id(db: Session, product_id: int):
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


def get_product_details(db: Session, product_id: int):
    return (
        db.query(Product)
        .options(joinedload(Product.category))
        .filter(Product.id == product_id)
        .first()
    )


def delete_product(db: Session, product_id: int):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        return None

    db.delete(product)
    db.commit()

    return product


def get_cheapest_product(db: Session):
    return (
        db.query(Product)
        .order_by(Product.price.asc())
        .first()
    )