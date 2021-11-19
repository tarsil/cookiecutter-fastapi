#!/usr/bin/env python
import os

import uvicorn

from src.main import get_settings


if __name__ == "__main__":
    """
    Sets a default `FASTAPI_SETTINGS_MODULE` settings configuration and loads accordingly.
    """
    if not os.getenv("FASTAPI_SETTINGS_MODULE"):
        os.environ["FASTAPI_SETTINGS_MODULE"] = "core.configs.settings"

    settings = get_settings()
    uvicorn.run('src.main:app', debug=os.getenv('DEBUG', settings.debug), port=os.getenv('PORT', settings.port),
                host=os.getenv('HOST', settings.host), reload=settings.reload, lifespan="off",
                log_level="info")
