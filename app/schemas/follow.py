from pydantic import BaseModel


class FollowUser(BaseModel):
    username: str
