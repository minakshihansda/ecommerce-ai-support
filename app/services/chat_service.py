from sqlalchemy.orm import Session, joinedload

from app.db.models.product import Product
from app.llm.groq_provider import generate_response


def get_ai_response(message: str, db: Session):

    products = (
        db.query(Product)
        .options(joinedload(Product.category))
        .all()
    )

    if products:
        product_information = "\n".join(
            [
                (
                    f"ID: {p.id}, "
                    f"Name: {p.name}, "
                    f"Price: Rs. {p.price}, "
                    f"Category: {p.category.name if p.category else 'Not available'}"
                )
                for p in products
            ]
        )
    else:
        product_information = "No products are currently available."

    prompt = f"""
You are an e-commerce customer support assistant.

Available products:

{product_information}

Answer the customer's question using the product information above.

Customer question:
{message}

Keep the answer short, clear and helpful.
If the requested information is not available, say that you don't have that information.
Do not invent product names, prices or categories.
"""

    return generate_response(prompt)