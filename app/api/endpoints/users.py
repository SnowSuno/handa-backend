from fastapi import APIRouter, Depends
from app import schemas
from app.core.dependancies import get_current_user


router = APIRouter(
    responses={401: {}}
)

@router.get("/me", response_model=schemas.User)
async def read_current_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user
