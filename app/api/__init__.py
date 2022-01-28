from fastapi import APIRouter

from app.api.endpoints import auth, users, todos, files

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(users.router, prefix="/users")
router.include_router(todos.router, prefix="/todos", tags=["todos"])
router.include_router(files.router, prefix="/files", tags=["files"])
