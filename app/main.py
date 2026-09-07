from fastapi import FastAPI

from app.api.v1.router import router

app = FastAPI(title="E-Commerce AI Support")

app.include_router(router)