from fastapi import APIRouter

from models.schemas import ContactBase, CallLogBase


router = APIRouter()


@router.get("/log/{call_id}")
async def get_call(call_id):
    return call_id


@router.get("/logs")
async def get_call_list():
    return {"message": []}


@router.post("/log")
async def create_call_log(call_log: CallLogBase):
    return call_log