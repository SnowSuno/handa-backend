from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app import schemas

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> schemas.User:
    return token
