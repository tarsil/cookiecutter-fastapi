"""
Main module for the routes of the app.
Imports all the remaining modules routes via `import` module name
"""

from fastapi_utils.inferring_router import InferringRouter
from .apps.{{ cookiecutter.app_name }}.v1.routes import routetr as router_v1

router = InferringRouter()
router.include_router(router_v1)
