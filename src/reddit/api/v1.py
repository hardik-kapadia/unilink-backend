from fastapi import APIRouter, Depends
from src.reddit.utils import RedditWrapper
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pprint import pprint

reddit_router = APIRouter(prefix="/reddit")

reddit_service = RedditWrapper()


@reddit_router.get("/")
def get_reddit():
    return "reddit app created!"


@reddit_router.get("/authorize/{code}")
def authorize_reddit_user(code):
    print(f"code {code}")
    res = ""
    try:
        res = reddit_service.autthorise_user(code)
        print(f"res: {res}")
        me = reddit_service.create_instance_using_refresh_token(
            refresh_token=res, access_token=code
        )
        print(f"me: {me}")
    except Exception as e:
        print(e)
    return JSONResponse(res)


@reddit_router.get("/posts/{subreddit}")
def get_posts(subreddit: str, category: str = "top"):
    print(subreddit)
    posts = reddit_service.get_top_post(subreddit)
    print(posts)
    # json_compatible_item_data = jsonable_encoder(posts)
    return JSONResponse(content=posts.__dict__)


@reddit_router.get("/user/{username}")
def get_user(username: str):
    print(f"pulling for user: {username}")
    redditor = reddit_service.get_redditor_by_username(username)
    return JSONResponse(redditor)


# @reddit_router.get('user/post/{post_content}')
# def user_post(post_content:str, reddit_service:RedditWrapper = Depends()):


@reddit_router.get("/user_subreddits")
def get_user_subreddits():
    res = reddit_service.get_user_subreddits()
    return JSONResponse(res)


@reddit_router.get("/submission/{subreddit}/{title}/{text}")
def create_post_on_subreddit(subreddit, title, text):
    res = reddit_service.post_on_subreddit(subreddit, title, text)
