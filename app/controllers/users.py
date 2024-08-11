from typing import Optional
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.users import UsersRepo
from core.database.session import get_session
from app.models.user import User
from core.controller.base import BaseController
from core.exceptions.base import ConflictException
from core.exceptions.base import NotFoundException


class UsersCtrl(BaseController):

    def __init__(self, session: AsyncSession = Depends(get_session)):
        super().__init__(session)
        self.users_repo = UsersRepo()

    async def create_user(
            self,
            user_id: int,
            username: Optional[str],
            first_name: Optional[str],
            last_name: Optional[str],
            language_code: Optional[str]
    ) -> User:
        user = await self.users_repo.get_by_id(
            self.session,
            user_id
        )
        if user:
            raise ConflictException("User already registered")
        user = await self.users_repo.create(
            self.session,
            attributes={
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "language_code": language_code
            }
        )
        await self.session.commit()
        return user

    async def get_user(
            self,
            user_id: int
    ) -> User:
        user: User = await self.users_repo.get_by_id(self.session, user_id)
        if not user:
            raise NotFoundException("User not found")
        return user
