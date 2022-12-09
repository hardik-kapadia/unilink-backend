from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_twitter():
    return "twitter app created!"
