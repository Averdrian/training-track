from fastapi import APIRouter, FastAPI, Request, Response

router = APIRouter()


@router.get("/health", status_code=200)
def health(response: Response):
    return {"detail": "ok"}
