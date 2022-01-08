import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette import status
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin import exceptions
from fakeredis import aioredis

from app import models

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

login_provider = UsernamePasswordProvider(
    admin_model=models.Admin,
    login_logo_url="https://preview.tabler.io/static/logo.svg"
)

def admin_init(app: FastAPI):
    admin_app.add_exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR, exceptions.server_error_exception)
    admin_app.add_exception_handler(status.HTTP_404_NOT_FOUND, exceptions.not_found_error_exception)
    admin_app.add_exception_handler(status.HTTP_403_FORBIDDEN, exceptions.forbidden_error_exception)
    admin_app.add_exception_handler(
        status.HTTP_401_UNAUTHORIZED,
        lambda *args: RedirectResponse("/admin/login")
    )

    @app.on_event("startup")
    async def startup():
        redis = aioredis.FakeRedis()
        await admin_app.configure(
            logo_url="https://preview.tabler.io/static/logo-white.svg",
            template_folders=[
                os.path.join(BASE_DIR, "templates")
            ],
            providers=[login_provider],
            redis=redis,
        )
    app.mount("/admin", admin_app)
