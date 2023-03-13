from fastapi import APIRouter

from app.routers.default import router as default_router
from app.routers.user import router as user_router

api_router = APIRouter()
api_router.include_router(router=default_router)
api_router.include_router(router=user_router)
