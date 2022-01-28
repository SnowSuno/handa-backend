from typing import Optional
from datetime import date

from pydantic import BaseModel, constr
from uuid import UUID


class TodoBase(BaseModel):
    title: constr(max_length=200)
    due_date: date

    class Config:
        orm_mode = True


class Todo(TodoBase):
    id: UUID
    is_done: bool


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    title: Optional[str] = None
    due_date: Optional[date] = None
    is_done: Optional[bool] = None
