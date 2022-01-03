from app import schemas, models
from app.core.security import hash_password

async def create_user(user: schemas.UserCreate):
    qwer = await models.User.create(
        **user.dict(),
        hashed_password=hash_password(user.password)
    )
    print(qwer)
    return qwer
