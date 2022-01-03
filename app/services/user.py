from app import models, schemas
from passlib.context import CryptContext


class UserManager:
    pwd_context: CryptContext

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    async def create_user(self, user: schemas.UserCreate):
        hashed_password = self.fake_hash(user.password)

        await models.User.create(
            username=user.username,
            hashed_password=hashed_password
        )

    async def authenticate_user(self):
        pass

    @staticmethod
    def fake_hash(password: str) -> str:
        return password


user_manager = UserManager()
