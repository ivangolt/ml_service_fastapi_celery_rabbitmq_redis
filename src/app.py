from fastapi import FastAPI
from loguru import logger

from src.api.routes.router import router as api_router


def get_app() -> FastAPI:
    """FastAPI initialization"""
    fastapi_app = FastAPI(
        title="Text tone classifier",
        version="0.1.0",
        debug=False,
        description="ML service for classifiying text tonality",
    )

    fastapi_app.include_router(api_router, prefix="/api")
    logger.info("FastAPI app has been initialized")
    return fastapi_app


app = get_app()
