"""
All the custom settings are placed here. The settings are therefore loaded
trough environment variable `FASTAPI_SETTINGS_FILENAME` that should be just a location
of the file.
"""
from fastapi_utils.api_settings import APISettings


class Settings(APISettings):
    """
    Base settings for the FastApi app
    """
    environment: str = "production"
    debug: bool = False
    title: str = "Awesome API"
    email_admin: str = "foobar@example.com"

settings = Settings()

def get_settings() -> Settings:
    return Settings()
