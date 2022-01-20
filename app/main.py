from fastapi import FastAPI, Depends
from app import api
from app.core.config import settings
from app.admin.init import admin_init
from app.db.database import db_init

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(api.router)

db_init(app)
admin_init(app)

