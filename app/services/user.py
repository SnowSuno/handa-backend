from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from email_validator import validate_email, EmailNotValidError
from app import schemas, models
from app.core.security import hash_password

async def create_user(user: schemas.UserCreate):
    return await models.User.create(
        **user.dict(),
        hashed_password=hash_password(user.password)
    )




