from ...configs.settings import Settings as MainSettings
from functools import lru_cache


class Settings(MainSettings):
    environment: str = 'testing'
    title: str = "Awesome API"
    debug: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
