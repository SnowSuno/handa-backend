from fastapi_users.db import TortoiseUserDatabase

from app.schemas.user import UserDB
from app.models.user import UserModel

async def get_user_db():
    yield TortoiseUserDatabase(UserDB, UserModel)
