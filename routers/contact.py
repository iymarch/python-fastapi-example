from fastapi import APIRouter
from ..models.schemas_models import Contact 


router = APIRouter()


@router.get("/contact/{contact_id}")
async def get_contact(contact_id: int):
    return {"message": contact_id}


@router.get("/contacts/")
async def get_contact_list():
    return {"message": []}


@router.post("/contact")
async def create_contact(contact: Contact):
    return {"message": contact}