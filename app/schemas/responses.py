from pydantic import BaseModel


class UserCheckResponse(BaseModel):
    is_available: bool
