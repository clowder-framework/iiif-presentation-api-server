
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="", tags=["utils"])


@router.get("/ok")
async def root():
    return {"status": "OK"}
