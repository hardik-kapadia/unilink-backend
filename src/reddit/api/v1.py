from fastapi import APIRouter, Depends
from src.reddit.utils import RedditWrapper
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pprint import pprint

reddit_router = APIRouter(prefix="/reddit")

reddit_router = APIRouter(prefix="/reddit")


@reddit_router.get("/")
def get_reddit():
    return "reddit app created!"


@reddit_router.get("/authosize/{code}")
def authorize_reddit_user(code: str, reddit_service: RedditWrapper = Depends()):
    print(f"code {code}")
    res = reddit_service.autthorise_user(code)
    return JSONResponse(res)


@reddit_router.get("/posts/{subreddit}")
def get_posts(
    subreddit: str, category: str = "top", reddit_service: RedditWrapper = Depends()
):
    print(subreddit)
    posts = reddit_service.get_top_post(subreddit)
    print(posts)
    # json_compatible_item_data = jsonable_encoder(posts)
    return JSONResponse(content=posts.__dict__)


@reddit_router.get("/user/{username}")
def get_user(username: str, reddit_service: RedditWrapper = Depends()):
    print(f"pulling for user: {username}")
    redditor = reddit_service.get_redditor_by_username(username)
    return JSONResponse(redditor)


@reddit_router.get("/user/subreddits")
def get_user_subreddits(reddit_service: RedditWrapper = Depends()):
    res = reddit_service.get_user_subreddits()
    return JSONResponse(res)
