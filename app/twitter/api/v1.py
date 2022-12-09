from fastapi import APIRouter

twitter_router = APIRouter(prefix="/twitter")


@twitter_router.get("/")
def get_twitter():
    return "twitter app created!"
