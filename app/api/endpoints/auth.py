from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas
from app.core.security import authenticate_user
from app.services.user import create_user
from app.services.registration import check_unique_fields_is_available

router = APIRouter()

@router.post(
    "/check-available",
    response_model=schemas.UserCheckResponse
)
async def check_user_unique(check: schemas.UserCheck):
    return schemas.UserCheckResponse(
        is_available=await check_unique_fields_is_available(check)
    )

@router.post(
    "/register",
    status_code=201,
    response_model=schemas.User,
    responses={400: {"description": "Already registered ID or email"}}
)
async def register_user(user: schemas.UserCreate):
    await check_unique_fields_is_available(user, auto_exception=True)
    return await create_user(user)


@router.post(
    "/login",
    response_model=schemas.Token,
    responses={401: {}}
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await authenticate_user(
        username=form_data.username,
        password=form_data.password
    )
    return token
