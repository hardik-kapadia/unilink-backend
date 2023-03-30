from fastapi import APIRouter,Depends
from src.facebook.utils import FacebookWrapper
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

facebook_router = APIRouter(prefix="/facebook")

@facebook_router.get("/")
def get_facebook():
    return "facebook app created!"

@facebook_router.get('/user_id')
def get_user_id(facebook_service : FacebookWrapper = Depends()):
    user_id = facebook_service.get_user_id()
    json_compatible_item_data = jsonable_encoder(user_id)
    return JSONResponse(content=json_compatible_item_data)

@facebook_router.get('/user_data')
def get_user_data(facebook_service : FacebookWrapper = Depends()):
    user_data = facebook_service.get_user_details()
    json_compatible_item_data = jsonable_encoder(user_data)
    return JSONResponse(content=json_compatible_item_data)

@facebook_router.get('/user_posts')
def get_user_data(facebook_service : FacebookWrapper = Depends()):
    user_posts = facebook_service.get_user_posts()
    json_compatible_item_data = jsonable_encoder(user_posts)
    return JSONResponse(content=json_compatible_item_data)

