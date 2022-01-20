from fastapi import APIRouter, Depends, UploadFile, File

from app import schemas, models
from app.core.dependancies import get_current_user

router = APIRouter()


@router.post("/test")
async def file_test(
    qwer: schemas.UserLogin,
    current_user: models.User = Depends(get_current_user),
    file: UploadFile = File(...),

):

    return {}
