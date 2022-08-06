import os
import sys
from pathlib import Path

Path(__file__).resolve().parent.parent.parent.parent
SITE_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
)
sys.path.append(SITE_ROOT)
sys.path.append(os.path.join(SITE_ROOT, "apps"))


DATABASES = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "postgres",
                "password": "postgres",
                "database": "piloto",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["accounts.models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}
