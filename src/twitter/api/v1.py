from fastapi import APIRouter

from src.main import twitter_service as twtsrvc

twitter_router = APIRouter(prefix="/twitter")

@twitter_router.get("/")
async def get_twitter():
    return "twitter app created!"


@twitter_router.get("/user/{username}")
async def get_user(username: str):
    twtsrvc.get_user_data_from_username(username)
    print(f"pulling for user: {username}")
    return f"Data pulled for {username}"


@twitter_router.get("/tweets/{username}")
async def get_user_tweets(username: str):
    print(f"username rcvd - {username}")
    return "Data from user's tweets fetched"


@twitter_router.get("/login_receive")
async def twitter_auth(state: str, code: str):
    print(f"state: {state}")
    print(f"code: {code}")
