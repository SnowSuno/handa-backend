from fastapi import APIRouter
from app import schemas
from app.services.user import user_manager

router = APIRouter()


@router.post("/register")
async def register_user(user: schemas.UserCreate):
    """
    Register a new user
    """
    await user_manager.create_user(user)


