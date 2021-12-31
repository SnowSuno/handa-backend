from fastapi_users import models
from tortoise.contrib.pydantic import PydanticModel

from app.models.user import UserModel


class User(models.BaseUser):
    pass

class UserCreate(models.BaseUserCreate):
    pass

class UserUpdate(models.BaseUserUpdate):
    pass

class UserDB(User, models.BaseUserDB, PydanticModel):
    class Config:
        orm_mode = True
        orig_model = UserModel
