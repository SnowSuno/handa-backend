from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas, models
from app.services.user import create_user
from app.services.registration import check_unique_fields_is_available


router = APIRouter()


@router.post(
    "/register",
    status_code=201,
    response_model=schemas.User,
    responses={400: {"description": "Already registered ID or email"}}
)
async def register_user(user: schemas.UserCreate):
    await check_unique_fields_is_available(user, auto_exception=True)
    return await create_user(user)


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {}

