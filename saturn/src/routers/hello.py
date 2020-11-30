"""
Routes responsible the urls of the current namespace and imported in `.routes`.
"""

from fastapi_utils.inferring_router import InferringRouter
import src.hello.views


router = InferringRouter(prefix='/test', tags=['test'], responses={404: {'description': "Not Found"}})
router.add_api_route(path='/', endpoint=src.hello.views.WelcomeApiView)

