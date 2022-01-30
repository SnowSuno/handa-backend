from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    responses={401: {}},
    tags=["user"]
)


@router.get("/me", response_model=schemas.User)
async def read_current_user(current_user: models.User = Depends(get_current_user)):
    await current_user.fetch_related("followings", "followers")
    return current_user


@router.get("/me/detail", response_model=schemas.UserDetail)
async def read_current_user_detail(current_user: models.User = Depends(get_current_user)):
    await current_user.fetch_related("followings", "followers")
    return current_user


@router.get("/{username}", response_model=schemas.UserPublic)
async def read_user(username: str):
    return await models.User.get(username=username)


@router.get("/{username}/detail", response_model=schemas.UserPublicDetail)
async def read_user_detail(username: str):
    return await models.User.get(username=username)\
        .prefetch_related("followings", "followers")


@router.put("/me", response_model=schemas.User)
async def update_current_user(
        user: schemas.UserUpdate,
        current_user: models.User = Depends(get_current_user)
):
    await current_user.update_from_dict(
        user.dict(exclude_unset=True)
    )
    await current_user.save()
    return current_user
