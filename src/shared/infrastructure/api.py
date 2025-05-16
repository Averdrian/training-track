from fastapi import APIRouter, FastAPI, Request, Response

router = APIRouter()


@router.get("/health")
def health():
    return {"detail": "ok"}
