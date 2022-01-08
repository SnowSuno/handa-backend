from typing import Any
from starlette.requests import Request
from tortoise.queryset import QuerySet

from fastapi_admin.widgets import filters


class ForeignFieldSearch(filters.Search):
    key_field: str

    def __init__(self, key_field: str, *args, **kwargs):
        self.key_field = key_field
        super(ForeignFieldSearch, self).__init__(*args, **kwargs)

    async def get_queryset(self, request: Request, value: Any, qs: QuerySet):
        name = self.context.get("name")
        return qs.filter(**{f"{name}__{self.key_field}": value})
