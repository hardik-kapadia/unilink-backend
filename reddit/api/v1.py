from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_reddit():
    return "reddit app created!"
