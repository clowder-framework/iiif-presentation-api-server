from fastapi import APIRouter
from app.api.routes import manifests, utils

api_router = APIRouter()
api_router.include_router(manifests.router)
api_router.include_router(utils.router)
