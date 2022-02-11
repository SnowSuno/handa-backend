from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    responses={401: {}},
    tags=["user"]
)


@router.get(
    "/me",
    response_model=schemas.User,
    response_model_exclude_none=True)
async def read_current_user(
        detail: bool = False,
        current_user: models.User = Depends(get_current_user)
):
    if detail:
        await current_user.fetch_related("followings", "followers", "todos")
    return current_user


@router.get(
    "/{username}",
    response_model=schemas.UserPublic,
    response_model_exclude_none=True)
async def read_user(
        username: str,
        detail: bool = False,
):
    user = await models.User.get(username=username)
    if detail:
        await user.fetch_related("followings", "followers", "todos")
    return user


@router.put(
    "/me",
    response_model=schemas.User,
    response_model_exclude_none=True)
async def update_current_user(
        user: schemas.UserUpdate,
        current_user: models.User = Depends(get_current_user)
):
    await current_user.update_from_dict(
        user.dict(exclude_unset=True)
    )
    await current_user.save()
    return current_user
