from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user
from tortoise.expressions import Q

router = APIRouter(
    responses={401: {}},
    tags=["user"]
)


@router.get("/", response_model=list[schemas.User])
async def search_users(search: str):
    return await models.User.filter(
        Q(username__contains=search) |
        Q(nickname__contains=search)
    )


@router.get(
    "/me",
    response_model=schemas.User)
async def read_current_user(
        current_user: models.User = Depends(get_current_user)
):
    return current_user


@router.get(
    "/me/detail",
    response_model=schemas.UserWithDetail)
async def read_current_user_with_detail(
        current_user: models.User = Depends(get_current_user)
):
    await current_user.get_details()
    return current_user


@router.get(
    "/{username}",
    response_model=schemas.User)
async def read_user(username: str):
    user = await models.User.get(username=username)
    return user


@router.get(
    "/{username}/detail",
    response_model=schemas.UserWithDetail)
async def read_user_with_detail(username: str):
    user = await models.User.get(username=username)
    await user.get_details()
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
