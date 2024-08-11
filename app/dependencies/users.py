from fastapi import Depends
from fastapi import Security
from fastapi.security import APIKeyHeader

from core.exceptions.base import UnprocessableEntity
from app.dependencies.api_key import validate_api_key


user_id_header = APIKeyHeader(name='X-USER-ID', scheme_name="userID", auto_error=False)


async def get_user_id(
        user_id: str = Security(user_id_header),
        _: bool = Depends(validate_api_key)
) -> int:
    if user_id is None or not user_id.isdigit():
        raise UnprocessableEntity("Invalid user ID")
    return int(user_id)
