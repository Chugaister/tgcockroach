from fastapi import APIRouter
from fastapi import Security
from fastapi import Depends

from app.dependencies.users import get_user_id
from app.schemas.requests.users import RegisterUserScheme
from app.schemas.responses.users import UserResponse
from app.controllers.users import UsersCtrl

users_router = APIRouter(tags=["Users"])


@users_router.post("/")
async def register_user(
        register_user_scheme: RegisterUserScheme,
        user_id: int = Security(get_user_id),
        users_ctrl: UsersCtrl = Depends(UsersCtrl)
) -> UserResponse:
    user = await users_ctrl.create_user(
        user_id,
        register_user_scheme.username,
        register_user_scheme.first_name,
        register_user_scheme.last_name,
        register_user_scheme.language_code
    )
    return user


@users_router.get("/")
async def get_user(
        user_id: int = Security(get_user_id),
        users_ctrl: UsersCtrl = Depends(UsersCtrl)
) -> UserResponse:
    user = await users_ctrl.get_user(user_id)
    return user

