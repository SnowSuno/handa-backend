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


class Detail(BaseModel):
    desc: str
    num_posts: int
    num_followers: int
    num_followings: int


class User(UserBase):
    is_verified: bool
    registered_at: datetime
    detail: Optional[Detail]


class UserPublic(User):
    email: SecretStr


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    desc: Optional[str] = None
