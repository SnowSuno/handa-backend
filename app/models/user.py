from typing import TYPE_CHECKING, Optional

from fastapi import HTTPException
from tortoise import fields, models
from email_validator import validate_email, EmailNotValidError

from app import schemas
from app.core.security import hash_password, pwd_context, create_access_token

if TYPE_CHECKING:
    from .todo import Todo

class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=30, unique=True)
    email = fields.CharField(max_length=50, unique=True)
    nickname = fields.CharField(max_length=30)
    hashed_password = fields.CharField(max_length=200)
    is_verified = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    registered_at = fields.DatetimeField(auto_now=True)

    todos: fields.ReverseRelation["Todo"]

    def __str__(self):
        return self.username

    @classmethod
    async def register(cls, user: schemas.UserCreate):
        return await cls.create(
            **user.dict(),
            hashed_password=hash_password(user.password)
        )

    @classmethod
    async def authenticate(cls, username: str, password: str) -> schemas.Token:
        user = await cls.get_by_username_or_email(username)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User with such email or id does not exist",
            )
        if not pwd_context.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Incorrect password"
            )
        token = create_access_token(str(user.id))
        return schemas.Token(
            access_token=token,
            token_type="bearer"
        )

    @classmethod
    async def get_by_username_or_email(cls, identifier: str) -> Optional["User"]:
        try:
            valid = validate_email(identifier)
            return await cls.get(email=valid.email)
        except EmailNotValidError:
            return await cls.get_or_none(username=identifier)
