"""
Main module for the routes of the app.
Imports all the remaining modules routes via `import` module name
"""

from fastapi_utils.inferring_router import InferringRouter
import src.routers.hello

router = InferringRouter(prefix="/api/v1")
router.include_router(src.routers.hello.router)
