from enum import Enum
from typing import List, Optional
from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class TypeCall(Enum):
    """ 
    Enumerator type call
    """
    missed = 0
    outgoing = 1
    incoming = 2


class ContactBase(BaseModel):
    """ 
    Response pydantic model Contact
    """
    name: str
    phone_number: str
    email: Optional[EmailStr] = None
    date_birth: Optional[date] = None

    class Config:
        orm_mode = True


class CallLogBase(BaseModel):
    """ 
    Response pydantic model CallLog
    """
    type_call: TypeCall  
    time_session: int
    datetime_call: datetime
    contact: ContactBase


