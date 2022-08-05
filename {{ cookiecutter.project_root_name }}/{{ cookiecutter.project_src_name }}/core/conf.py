import importlib
import os


def get_settings(config: str = None):
    """
    The `config` is a module path in teh format of `core.configs.settings` or else it will load the default.
    """
    module = os.getenv("FASTAPI_SETTINGS_MODULE") or "core.configs.settings"

    try:
        config = config or module
        configs = importlib.import_module(config)
    except (ImportError, AttributeError):
        configs = importlib.import_module(module)

    settings = getattr(configs, "get_settings")
    return settings()


settings = get_settings()
