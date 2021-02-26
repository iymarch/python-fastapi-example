from fastapi import APIRouter
from sqlalchemy.orm import Session

from models.schemas import CallLogBase
from database import SessionLocal
from database import query
from dependencies.db import get_db


router = APIRouter()


@router.get("/log/{call_id}", response_model=CallLogBase)
async def get_call(call_id: int, session: Session = Depends(get_db)):
    return query.get_call_log(session, call_id)


@router.get("/logs", response_model=List[CallLogBase])
async def get_call_list(session: Session = Depends(get_db)):
    return query.get_all_call_logs(session)


@router.post("/log", response_model=CallLogBase)
async def create_call_log(contact: ContactBase, session: Session = Depends(get_db)):
    db_log = query.get_call_log_by_contact(session, contact_id=contact.id)
    if db_log:
        raise HTTPException(status_code=400, detail="Call log already exists")
    call_log_base = CallLogBase
    call_log_base.contact = contact
    return query.create_log(session, call_log_base)