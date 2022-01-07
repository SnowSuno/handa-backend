from typing import Any

from fastapi_admin.widgets import inputs
from starlette.requests import Request

from app.core.security import hash_password


class HashedPassword(inputs.Password):
    async def parse_value(self, request: Request, value: Any):
        print(value)
        return hash_password(value)
