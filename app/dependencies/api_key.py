from fastapi.security import APIKeyHeader
from fastapi import Security

from core.exceptions.base import UnauthorizedException
from server.config import config


api_key_header = APIKeyHeader(name="X-API-KEY", scheme_name="apiKey", auto_error=False)


async def validate_api_key(api_key: str = Security(api_key_header)) -> bool:
    if api_key != config.API_KEY:
        raise UnauthorizedException("Invalid API key")
    return True
