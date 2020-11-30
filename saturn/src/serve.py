#!/usr/bin/env python
import os

import uvicorn
from src.main import get_settings

if __name__ == "__main__":
    """
    Sets a default `FASTAPI_SETTINGS_MODULE` settings configuration and loads accordingly.
    """
    os.environ.setdefault("FASTAPI_SETTINGS_MODULE", "src.configs.settings")
    settings = get_settings()
    uvicorn.run('src.main:create_app', debug=os.getenv('DEBUG', settings.debug), port=os.getenv('PORT', settings.port),
                host=os.getenv('HOST', settings.host), reload=settings.reload)
