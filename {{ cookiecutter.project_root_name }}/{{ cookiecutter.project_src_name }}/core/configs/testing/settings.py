from ...configs.settings import Settings
from functools import lru_cache


class _Settings(Settings):
    environment: str = 'testing'
    title: str = "Awesome API"
    debug: bool = True


@lru_cache()
def get_settings() -> _Settings:
    return _Settings()
