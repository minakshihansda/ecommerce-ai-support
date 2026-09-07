from sqlalchemy.orm import Session

from app.db.models.product import Product
from app.llm.groq_provider import generate_response


def get_ai_response(message: str, db: Session):
    products = db.query(Product).all()

    product_information = "\n".join(
        [
            f"ID: {p.id}, Name: {p.name}, Price: ₹{p.price}"
            for p in products
        ]
    )

    prompt = f"""
You are an e-commerce customer support assistant.

Available products:

{product_information}

Answer the customer's question using the product information above.

Customer question:
{message}

Keep the answer short, clear and helpful.
If the requested information is not available, say that you don't have that information.
"""

    return generate_response(prompt)