from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.schemas import ContactBase
from database import SessionLocal
from database import query
from dependencies.db import get_db


router = APIRouter()


@router.get("/contact/{contact_id}", response_model=ContactBase)
async def get_contact(contact_id: int, session: Session = Depends(get_db)):
    return query.get_contact(session, contact_id)


@router.get("/contacts/", response_model=List[ContactBase])
async def get_contact_list(session: Session = Depends(get_db)):
    return query.get_all_contacts(session)


@router.post("/contact", response_model=ContactBase)
async def create_contact(contact: ContactBase, session: Session = Depends(get_db)):
    db_contact = query.get_contact_by_phone(session, phone_number=contact.phone_number)
    if db_contact:
        raise HTTPException(status_code=400, detail="Contact already exists")
    return query.create_contact(session, contact)