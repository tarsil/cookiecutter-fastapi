"""
Routes responsible the urls of the current namespace and imported in `.routes`.
"""

from fastapi.routing import APIRouter
import {{ cookiecutter.app_name }}.views

from starlette.routing import Route

router = APIRouter(prefix='/{{ cookiecutter.app_name }}', tags=['{{ cookiecutter.project_name }}'], responses={404: {'description': "Not Found"}})
router.add_api_route('/', {{ cookiecutter.app_name }}.views.welcome)
router.add_api_route('/{name}', {{ cookiecutter.app_name }}.views.welcome_name)
