from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt, JWTError

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
