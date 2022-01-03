from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas
from app.services.user import user_manager

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(user: schemas.UserCreate):
    """
    Register a new user
    """
    await user_manager.create_user(user)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {}

