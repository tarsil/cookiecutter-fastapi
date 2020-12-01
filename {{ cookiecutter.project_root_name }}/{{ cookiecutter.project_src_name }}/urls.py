"""
Main module for the routes of the app.
Imports all the remaining modules routes via `import` module name
"""

from fastapi_utils.inferring_router import InferringRouter
import routers.{{ cookiecutter.app_name }}

router = InferringRouter(prefix="/api/v1")
router.include_router(routers.{{ cookiecutter.app_name }}.router)
