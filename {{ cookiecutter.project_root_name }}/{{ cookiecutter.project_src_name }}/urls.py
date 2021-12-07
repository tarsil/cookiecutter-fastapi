"""
Main module for the routes of the app.
Imports all the remaining modules routes via `import` module name
"""

from fastapi_utils.inferring_router import InferringRouter
import .apps.{{ cookiecutter.app_name }}.v1.routes

router = InferringRouter()
router.include_router({{ cookiecutter.app_name }}.v1.routes.router)
