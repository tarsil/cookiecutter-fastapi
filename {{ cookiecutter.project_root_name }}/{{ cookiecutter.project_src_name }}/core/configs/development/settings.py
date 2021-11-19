from ..settings import Settings
from functools import lru_cache


class _Settings(Settings):
    environment: str = 'development'
    title: str = "Awesome API - Development"
    debug: bool = True
    port: int = 8002
    reload: bool = True
    host='0.0.0.0'


@lru_cache()
def get_settings() -> _Settings:
    return _Settings()
