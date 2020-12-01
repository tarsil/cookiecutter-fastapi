from starlette.responses import JSONResponse
from fastapi.requests import Request


def welcome(request: Request):
    return JSONResponse({'name': 'Welcome'})


def welcome_name(request: Request, name: str):
    return JSONResponse({'name': name})
