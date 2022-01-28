from fastapi import APIRouter, Depends
from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter(
    responses={401: {}},
    tags=["user"]
)


@router.get("/me", response_model=schemas.User)
async def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.get("/{username}", response_model=schemas.UserPublicOut)
async def read_user(username: str):
    return await models.User.get(username=username)


@router.put("/me")
async def update_current_user(
        user: schemas.UserUpdate,
        current_user: models.User = Depends(get_current_user)
):
    # TODO
    return {"message": "Not implemented yet"}
