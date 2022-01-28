from fastapi import APIRouter
from . import api, follows, todos

router = APIRouter()

router.include_router(api.router)
router.include_router(follows.router)
router.include_router(todos.router)
