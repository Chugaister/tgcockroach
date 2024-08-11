from pydantic import Field
from app.schemas.base.users import UserBase
from pydantic import PositiveInt


class UserResponse(UserBase):
    user_id: PositiveInt = Field()
