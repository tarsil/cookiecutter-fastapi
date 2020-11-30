from src.configs.settings import Settings


class Settings(Settings):
    environment: str = 'testing'
    title: str = "Awesome API"
    debug: bool = True

settings = Settings()
