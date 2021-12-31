from fastapi import APIRouter

from app.core.users import auth_backend, current_active_user, fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/jwt"
)

router.include_router(fastapi_users.get_register_router())
router.include_router(fastapi_users.get_reset_password_router())
router.include_router(fastapi_users.get_verify_router())

