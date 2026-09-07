from fastapi import APIRouter

from app.api.v1.endpoints import health, products, chat, users

router = APIRouter()

router.include_router(health.router)
router.include_router(products.router)
router.include_router(chat.router)
router.include_router(users.router)