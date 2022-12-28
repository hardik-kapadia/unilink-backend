from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.twitter.utils import TwitterWrapper

# from ...main import twitter_service as twtsrvc

twitter_router = APIRouter(prefix="/twitter")

@twitter_router.get("/")
async def get_twitter():
    return "twitter app created!"


@twitter_router.get("/user/{username}")
async def get_user(username: str,twitter_service : TwitterWrapper = Depends()):
    
    user_data = twitter_service.get_user_data_from_username(username)
    json_compatible_item_data = jsonable_encoder(user_data)
    return JSONResponse(content=json_compatible_item_data)


@twitter_router.get("/tweets/{username}")
async def get_user_tweets(username: str):
    print(f"username rcvd - {username}")
    return "Data from user's tweets fetched"


@twitter_router.get("/login_receive")
async def twitter_auth(state: str, code: str):
    print(f"state: {state}")
    print(f"code: {code}")
