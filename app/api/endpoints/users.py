from typing import List

from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user


router = APIRouter(
    responses={401: {}}
)

@router.get("/me", response_model=schemas.User)
async def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.get("/me/todos", response_model=List[schemas.Todo])
async def read_todos_of_current_user(current_user: models.User = Depends(get_current_user)):
    return await current_user.todos
