from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    """ 
    Response pydantic model Contact
    """
    name: str
    phone_number: str
    email: Optional[EmailStr] = None
    date_year = Optional[datetime] = None
