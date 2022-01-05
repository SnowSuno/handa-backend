import os

from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fakeredis import aioredis

from app import models

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

login_provider = UsernamePasswordProvider(
    admin_model=models.Admin,
    login_logo_url="https://preview.tabler.io/static/logo.svg"
)

def admin_init(app: FastAPI):
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
