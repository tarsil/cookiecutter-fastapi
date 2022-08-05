import importlib
import os

from fastapi_utils.api_settings import APISettings
from loguru import logger


def get_settings(config: str = None) -> APISettings:
    """
    The `config` is a module path in teh format of `core.configs.settings` or else it will load the default.
    """
    module = os.getenv("FASTAPI_SETTINGS_MODULE") or "core.configs.settings"

    try:
        config = config or module
        configs = importlib.import_module(config)
    except (ImportError, AttributeError):
        configs = importlib.import_module(module)

    settings = getattr(configs, "get_settings", None)
    if not settings:
        logger.warning(f"get_settings() not found in {module}.")
        logger.warning("Default to base APISettings.")
        settings = APISettings

    return settings()


settings = get_settings()
