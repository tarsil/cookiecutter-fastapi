"""
Routes responsible the urls of the current namespace and imported in `.routes`.
"""

from fastapi.routing import APIRouter

from .views import welcome

router = APIRouter(
    prefix="/api/v1/accounts",
    tags=["Accounts"],
    responses={404: {"description": "Not Found"}},
)
router.add_api_route("/", welcome)
