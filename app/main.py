from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq


# Load environment variables
load_dotenv("app/.env")

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


app = FastAPI(title="E-Commerce AI Support")


# Chat request schema
class ChatRequest(BaseModel):
    message: str


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# Products
@app.get("/products")
def products():
    return [
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


# Cheapest product
@app.get("/products/cheapest")
def cheapest_product():
    products_list = products()

    cheapest = min(products_list, key=lambda x: x["price"])

    return cheapest


# Get product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):

    products_list = products()

    for product in products_list:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}


# AI Chat
@app.post("/chat")
def chat(request: ChatRequest):

    try:
        products_list = products()

        product_information = "\n".join(
            [
                f"ID: {p['id']}, Name: {p['name']}, Price: ₹{p['price']}"
                for p in products_list
            ]
        )

        prompt = f"""
You are an e-commerce customer support assistant.

Here are the available products:

{product_information}

Answer the customer's question using the product information above.

Customer question:
{request.message}

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

        answer = response.choices[0].message.content

        return {
            "answer": answer
        }

    except Exception as e:

        return {
            "error": "Sorry, the AI service is temporarily unavailable.",
            "details": str(e)
        }