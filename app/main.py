from fastapi import FastAPI
from app import api
from app.db.database import db_init

# def create_app() -> FastAPI:
#
#
#     return _app
#
#
# app = create_app()

app = FastAPI()
app.include_router(api.router)

db_init(app)
