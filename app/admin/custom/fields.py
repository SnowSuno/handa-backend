from typing import Type

from starlette.requests import Request
from tortoise.models import Model
from fastapi_admin.resources import ComputeField


class ForeignKeyDisplayField(ComputeField):
    model: Type[Model]
    display_field: str

    def __init__(self, model: Type[Model], display_field: str, *args, **kwargs):
        self.model = model
        self.display_field = display_field
        self._cache = {}
        super(ForeignKeyDisplayField, self).__init__(*args, **kwargs)

    async def get_value(self, request: Request, obj: dict):
        return await self.get_related_model(obj.get(self.name))

    async def get_related_model(self, id_):
        if id_ not in self._cache:
            await self.refresh_cache()
        return self._cache.get(id_)

    async def refresh_cache(self):
        self._cache = {
            model.pk: getattr(model, self.display_field)
            for model in await self.model.all()
        }
