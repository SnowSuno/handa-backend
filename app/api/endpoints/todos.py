from typing import List

from fastapi import APIRouter
from app.schemas.todo import Todo

router = APIRouter()


@router.get("/", response_model=Todo)
def read_todos() -> List[Todo]:
    return []
