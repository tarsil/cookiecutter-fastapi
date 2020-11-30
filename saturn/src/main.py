import importlib
import os

from fastapi import FastAPI
from fastapi_utils.api_settings import get_api_settings
from fastapi_utils.api_settings import APISettings


def configure_app(app: FastAPI) -> None:
    """
    The configuration is read from the filename in the "FASTAPI_SETTINGS_MODULE"
    environment variable (if it exists) and some other important settings.

    We activate the routing here to make sure everything runs smoothly but some additional configurations can also
    be added.

    :param FastAPI app: The FastAPI app that requires configuring.
    :return: None
    """
    from .router import router as router_v1
    app.include_router(router_v1)


def get_settings(config: str=None) -> APISettings:
    try:
        configs = importlib.import_module(config)
    except (ImportError, AttributeError):
        configs = importlib.import_module(os.getenv('FASTAPI_SETTINGS_MODULE'))
    return configs.settings


def create_app(config: str=None):
    """
    Main entry-point of the service.
    Initializes the service and all the dependencies

    1. Creates the scaffold app
    2. Initializes the dependencies and add them to the application context
    """
    get_api_settings.cache_clear()
    settings = get_settings(config)
    app = FastAPI(**settings.fastapi_kwargs)
    configure_app(app)

    return app
