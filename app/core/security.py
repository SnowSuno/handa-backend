from typing import Optional
from datetime import datetime, timedelta

from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from email_validator import validate_email, EmailNotValidError

from app import schemas, models
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"])

class TokenError(Exception):
    pass

def create_access_token(uuid: str) -> str:
    expire = datetime.utcnow() + timedelta(
        days=settings.ACCESS_TOKEN_EXPIRE_DAYS
    )
    return jwt.encode(
        {"sub": uuid, "exp": expire},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def decode_access_token(token: str) -> str:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        expire = payload.get("exp")
        if expire is None or datetime.now() >= datetime.fromtimestamp(expire):
            raise TokenError

        user_id = payload.get("sub")
        if user_id is None:
            raise TokenError
        return user_id

    except JWTError:
        raise TokenError


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def get_user_by_username_or_email(username: str) -> Optional[models.User]:
    try:
        valid = validate_email(username)
        return await models.User.get(email=valid.email)
    except EmailNotValidError:
        return await models.User.get_or_none(username=username)

async def authenticate_user(username: str, password: str) -> schemas.Token:
    user = await get_user_by_username_or_email(username)
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
