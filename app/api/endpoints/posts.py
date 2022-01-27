from fastapi import APIRouter, Depends

from app import models
from app.core.dependancies import get_current_user

router = APIRouter()


@router.post("/")
async def create_post(
    current_user: models.User = Depends(get_current_user),

):
    pass
