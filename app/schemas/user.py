from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
from app import models

class UserCheck(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class UserBase(BaseModel):
    username: str
    email: EmailStr
    nickname: str

    class Config:
        orm_mode = True

class User(UserBase):
    is_verified: bool
    registered_at: datetime

# class UserWithToken(User):
#     access_token: str
#     token_type: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    nickname: Optional[str] = None


UserDB = pydantic_model_creator(models.User)
