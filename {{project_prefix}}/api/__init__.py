from fastapi import FastAPI

from api.endpoints import router, health
from core.config import settings


def get_app() -> FastAPI:
    server = FastAPI(
        title=settings.project_name,
        openapi_url=settings.openapi_route,
        debug=settings.debug,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
    )

    server.include_router(router, prefix=settings.api_v1_route)
    server.include_router(health.router, tags=["health"])

    return server
