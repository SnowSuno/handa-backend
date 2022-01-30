from typing import Optional

from pydantic import BaseModel, EmailStr, constr, SecretStr
from datetime import datetime


class UserCheck(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


class UserBase(BaseModel):
    username: constr(max_length=30)
    email: EmailStr
    nickname: constr(max_length=30)

    class Config:
        orm_mode = True


class User(UserBase):
    desc: str
    is_verified: bool
    registered_at: datetime


class UserPublicOut(User):
    email: SecretStr


class UserPublicIn(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    desc: Optional[str] = None
