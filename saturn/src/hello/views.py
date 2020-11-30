from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse


class WelcomeApiView(HTTPEndpoint):
    """
    Welcome API for the given parameters of the `cookicutter-fastapi`
    """
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")


