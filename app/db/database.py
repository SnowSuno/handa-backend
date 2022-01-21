from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings

TORTOISE_ORM = {
    'connections': {
        'default': settings.DATABASE_URL,
    },
    'apps': {
        'models': {
            'models': ["app.models", "aerich.models"],
            'default_connection': 'default',
        }
    }
}


def db_init(app: FastAPI):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )
