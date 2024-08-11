from core.repository.base import BaseRepository
from app.models.user import User


class UsersRepo(BaseRepository):

    def __init__(self):
        super().__init__(User)
