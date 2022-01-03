from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class User(UserBase):
    pass

class UserWithToken(User):
    token: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str
