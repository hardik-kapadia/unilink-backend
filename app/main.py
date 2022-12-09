from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .reddit.api.v1 import reddit_router
from .twitter.api.v1 import twitter_router

from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    _app.include_router(router=reddit_router)
    _app.include_router(router=twitter_router)

    return _app


app = get_application()
