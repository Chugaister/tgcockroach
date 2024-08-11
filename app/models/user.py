from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT
from uuid import uuid4
from sqlalchemy import String

from core.database.base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BIGINT, primary_key=True, default=uuid4)
    username = Column(String(32), unique=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64))
    language_code = Column(String(32))
