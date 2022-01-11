from fastapi import FastAPI
from piccolo.engine import engine_finder

from app.core.config import settings

def db_init(app: FastAPI):
    @app.on_event("startup")
    async def open_database_connection_pool():
        engine = engine_finder(module_name=settings.PICCOLO_CONF)
        await engine.start_connnection_pool()

    @app.on_event("shutdown")
    async def close_database_connection_pool():
        engine = engine_finder(module_name=settings.PICCOLO_CONF)
        await engine.close_connnection_pool()
