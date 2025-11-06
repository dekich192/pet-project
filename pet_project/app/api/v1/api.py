from fastapi import APIRouter

from .endpoints import auth, workers

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(workers.router, prefix="/api/v1", tags=["workers"])
