from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv("app/.env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


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

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful e-commerce support assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content