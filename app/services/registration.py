from fastapi import HTTPException
from app import schemas, models

async def check_username_is_available(username: str, auto_exception: bool = False) -> bool:
    is_available = not bool(await models.User.get_or_none(username=username))
    if auto_exception and not is_available:
        raise HTTPException(
            status_code=400,
            detail="An user with this id already exists"
        )
    return is_available

async def check_email_is_available(email: str, auto_exception: bool = False) -> bool:
    is_available = not bool(await models.User.get_or_none(email=email))
    if auto_exception and not is_available:
        raise HTTPException(
            status_code=400,
            detail="An user with this email already exists"
        )
    return is_available

async def check_unique_fields_is_available(user: schemas.UserCreate, auto_exception: bool = False):
    username_is_available = await check_username_is_available(user.username, auto_exception=auto_exception)
    email_is_available = await check_email_is_available(user.email, auto_exception=auto_exception)
    return username_is_available and email_is_available
