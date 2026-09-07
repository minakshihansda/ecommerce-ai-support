from fastapi import FastAPI

from app.api.v1.endpoints import health, products, chat

app = FastAPI(title="E-Commerce AI Support")

app.include_router(health.router)
app.include_router(products.router)
app.include_router(chat.router)