from fastapi import APIRouter

reddit_router = APIRouter(prefix="/reddit")


@reddit_router.get("/")
def get_reddit():
    return "reddit app created!"
