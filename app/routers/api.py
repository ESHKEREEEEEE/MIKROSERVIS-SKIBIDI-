from fastapi import APIRouter

from .v1.requests import requests

api_router = APIRouter()

api_router.include_router(requests.router, tags=["Requests"], prefix="/requests")
