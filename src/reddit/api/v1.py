from fastapi import APIRouter

reddit_router = APIRouter(prefix="/reddit")


@reddit_router.get("/")
def get_reddit():
    return "reddit app created!"


@reddit_router.get("/posts/{subreddit}")
def get_posts(subreddit: str, category: str = "top"):
    print(f"subreddit rcvd - {subreddit}")
    print(f"category = {category}")
    return "Data from subreddit fetched"


@reddit_router.get("/user/{username}")
def get_user(username: str):
    print(f"pulling for user: {username}")
    return "Data pulled for username"


@reddit_router.get("/user/{username}/posts")
def get_user_posts(username: str, max_posts: int = 10):
    print(f"username: - {username}")
    print(f"max_posts - {max_posts}")
    return f"{max_posts} Posts pulled from {username}"
