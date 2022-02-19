from fastapi import APIRouter, Depends, HTTPException
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    tags=["user - follows"]
)


@router.get(
    "/me/followings",
    response_model=list[schemas.User])
async def read_followings_of_current_user(current_user: models.User = Depends(get_current_user)):
    return await current_user.followings


@router.post(
    "/me/followings/{username}",
    response_model=schemas.User,
    responses={404: {}, 400: {}})
async def follow_user(
        username: str,
        current_user: models.User = Depends(get_current_user),
):
    user_obj = await models.User.get(username=username)
    if user_obj == current_user:
        raise HTTPException(
            status_code=400,
            detail="Cannot follow self"
        )

    await current_user.followings.add(user_obj)
    return user_obj


@router.delete("/me/followings/{username}", status_code=204)
async def unfollow_user(
        username: str,
        current_user: models.User = Depends(get_current_user),
):
    user_obj = await models.User.get(username=username)
    await current_user.followings.remove(user_obj)


@router.get(
    "/{username}/followings",
    response_model=list[schemas.User])
async def read_followings(username: str):
    user_obj = await models.User.get(username=username)
    return await user_obj.followings


@router.get(
    "/me/followers",
    response_model=list[schemas.User])
async def read_followers_of_current_user(current_user: models.User = Depends(get_current_user)):
    return await current_user.followers


@router.delete(
    "/me/followers/{username}", status_code=204)
async def delete_follower_of_current_user(
        username: str,
        current_user: models.User = Depends(get_current_user)):
    user_obj = await models.User.get(username=username)
    await current_user.followers.remove(user_obj)


@router.get(
    "/{username}/followers",
    response_model=list[schemas.User])
async def read_followers(username: str):
    user_obj = await models.User.get(username=username)
    return await user_obj.followers
