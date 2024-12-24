from fastapi import APIRouter
from .name_routes import router as name_router

# 创建根路由
api_router = APIRouter()

# 注册子路由
api_router.include_router(name_router)
