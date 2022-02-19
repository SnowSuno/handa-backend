from typing import Union, Optional

from fastapi import HTTPException
from app import schemas, models


async def check_username_is_available(username: Optional[str], auto_exception: bool = False) -> bool:
    if username is None:
        return True
    is_available = not bool(await models.User.get_or_none(username=username))
    if auto_exception and not is_available:
        raise HTTPException(
            status_code=400,
            detail="An user with this id already exists"
        )
    return is_available


async def check_email_is_available(email: Optional[str], auto_exception: bool = False) -> bool:
    if email is None:
        return True
    is_available = not bool(await models.User.get_or_none(email=email))
    if auto_exception and not is_available:
        raise HTTPException(
            status_code=400,
            detail="An user with this email already exists"
        )
    return is_available


async def check_unique_fields_is_available(
        user: Union[schemas.UserCreate, schemas.UserCheck],
        auto_exception: bool = False
) -> bool:
    username_is_available = await check_username_is_available(user.username, auto_exception=auto_exception)
    email_is_available = await check_email_is_available(user.email, auto_exception=auto_exception)
    return username_is_available and email_is_available
