from app.llm.groq_provider import generate_response


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


def get_ai_response(message: str):
    product_information = "\n".join(
        [
            f"ID: {p['id']}, Name: {p['name']}, Price: ₹{p['price']}"
            for p in PRODUCTS
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