from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class UserBase(BaseModel):
    username: Optional[str] = Field()
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    language_code: Optional[str] = Field()
