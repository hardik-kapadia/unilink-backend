from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.twitter.utils import TwitterWrapper

from src.reddit.api.v1 import reddit_router

from src.twitter.api.v1 import twitter_router

from src.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    version = settings.VERSION

    common_prefix = "/api/v" + str(version)

    _app.include_router(router=reddit_router, prefix=common_prefix)
    _app.include_router(router=twitter_router, prefix=common_prefix)

    return _app

twitter_service = TwitterWrapper()

app = get_application()
