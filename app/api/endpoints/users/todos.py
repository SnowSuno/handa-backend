from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    tags=["user - todos"]
)


@router.get("/me/todos", response_model=list[schemas.Todo])
async def read_todos_of_current_user(current_user: models.User = Depends(get_current_user)):
    return await current_user.todos
