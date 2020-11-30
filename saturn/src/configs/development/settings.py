from src.configs.settings import *


class Settings(Settings):
    environment: str = 'development'
    title: str = "Awesome API"
    debug: bool = True
    port: int = 8001
    reload: bool = True
    host='0.0.0.0'

settings = Settings()
