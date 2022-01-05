from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app import models
from app.core.security import decode_access_token, TokenError

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> models.User:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        user_id = decode_access_token(token)
    except TokenError:
        raise credentials_exception

    user = await models.User.get_or_none(id=user_id)
    if user is None:
        raise credentials_exception

    return user
