from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    id: str
    email: EmailStr
    nickname: str

class User(UserBase):
    is_verified: bool
    registered_at: datetime

class UserWithToken(User):
    token: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str
