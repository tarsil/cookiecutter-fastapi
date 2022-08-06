from fastapi.requests import Request
from starlette.responses import JSONResponse

from ..models import User


async def welcome(request: Request):

    return JSONResponse({"name": "Welcome to accounts"})
