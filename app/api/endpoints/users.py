from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user


router = APIRouter(
    responses={401: {}}
)

@router.get("/me", response_model=schemas.User)
async def read_current_user(current_user: models.User = Depends(get_current_user)):
    print(current_user.hashed_password)
    return current_user
