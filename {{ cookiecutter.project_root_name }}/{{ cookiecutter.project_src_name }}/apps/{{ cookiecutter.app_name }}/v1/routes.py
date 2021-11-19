"""
Routes responsible the urls of the current namespace and imported in `.routes`.
"""

from fastapi.routing import APIRouter
from .views import welcome, welcome_name


router = APIRouter(prefix='/api/v1', tags=['my-fastapi-app'], responses={404: {'description': "Not Found"}})
router.add_api_route('/', welcome)
router.add_api_route('/{name}', welcome_name)
