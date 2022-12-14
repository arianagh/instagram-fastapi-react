from app.api.routers import user
from app.api.routers import post
from app.api.routers import auth
from app.api.routers import comment
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(post.router)
api_router.include_router(auth.router)
api_router.include_router(comment.router)
