from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, Enum

from database import Base
from models.schemas import TypeCall


class Contact(Base):
    """
    Database model Contact
    """
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, default=None)
    date_birth = Column(Date, default=None)
    call_log = relationship("CallLog")


class CallLog(Base):
    """ 
    Database model CallLog
    """
    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True, index=True)
    type_call = Column(Enum(TypeCall)) 
    time_session = Column(Integer)
    datetime_call = Column(DateTime)
    contact = Column(Integer, ForeignKey("contacts.id"))