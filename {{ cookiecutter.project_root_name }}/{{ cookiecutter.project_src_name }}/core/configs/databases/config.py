import os
from typing import Type

from tortoise.models import Model


class DefaultRouter:
    def db_for_read(self, model: Type[Model]):
        return "default"

    def db_for_write(self, model: Type[Model]):
        return "default"


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.environ.get("POSTGRES_HOST", "localhost"),
                "port": os.environ.get("POSTGRES_PORT", "5432"),
                "user": os.environ.get("POSTGRES_USER", "postgres"),
                "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
                "database": os.environ.get(
                    "POSTGRES_PASSWORD", "{{ cookiecutter.project_name }}"
                ),
            },
        },
    },
    "apps": {
        "accounts": {
            "models": ["accounts.models", "aerich.models"],
            "connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}
