from fastapi import APIRouter

from app.core.users import fastapi_users

router = APIRouter()

router.include_router(fastapi_users.get_users_router())

# @router.get("/")
# def read_users():
#     return {}
