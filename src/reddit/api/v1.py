from fastapi import APIRouter,Depends
from src.reddit.utils import RedditWrapper
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
reddit_router = APIRouter(prefix="/reddit")

reddit_router = APIRouter(prefix="/reddit")


@reddit_router.get("/")
def get_reddit():
    return "reddit app created!"


@reddit_router.get("/posts/{subreddit}")
def get_posts(subreddit: str, category: str = "top",reddit_service:RedditWrapper=Depends()):
    print(subreddit)
    posts = reddit_service.get_top_post(subreddit)
    print(posts)
    json_compatible_item_data = jsonable_encoder(posts)
    return JSONResponse(content=json_compatible_item_data)



@reddit_router.get("/user/{username}")
def get_user(username: str,reddit_service:RedditWrapper=Depends()):
    print(f"pulling for user: {username}")
    redditor = reddit_service.get_redditor_by_username(username)
    return "Data pulled for username"


@reddit_router.get("/user/{username}/posts")
def get_user_posts(username: str, max_posts: int = 10,reddit_service:RedditWrapper=Depends()):
    print(f"username: - {username}")
    print(f"max_posts - {max_posts}")
    
    return f"{max_posts} Posts pulled from {username}"
