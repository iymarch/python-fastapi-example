from sqlalchemy.orm import Session

from models import db, schemas


def get_contact(session: Session, contact_id: int):
    return session.query(db.Contact).filter(db.Contact.id == contact_id).first()


def get_contact_by_phone(session: Session, phone_number: str):
    return session.query(db.Contact).filter(db.Contact.phone_number == phone_number).first()


def get_all_contacts(session: Session):
    return session.query(db.Contact).filter().all()
    

def create_contact(session: Session, contact: schemas.ContactBase):
    db_contact = db.Contact(name=contact.name, 
                            email=contact.email,
                            phone_number=contact.phone_number,
                            date_birth=contact.date_birth)
    session.add(db_contact)
    session.commit()
    session.refresh(db_contact)
    return db_contact


def get_call_log(session: Session, call_log_id: int):
    return session.query(db.CallLog).filter(db.CallLog.id == call_log_id).first()


def get_call_log_by_contact(session: Session, contact_id: int):
    return session.query(db.CallLog).filter(db.CallLog.contact == contact_id).first()


def get_all_call_logs(session: Session):
    return session.query(db.CallLog).filter().all()
    

def create_call_log(session: Session, call_log: schemas.CallLogBase):
    db_call_log = db.Contact(type_cal=call_log.type_call, 
                            time_session=call_log.time_session,
                            datetime_call=call_log.datetime_call,
                            contact=call_log.contact)
    session.add(db_call_log)
    session.commit()
    session.refresh(db_call_log)
    return db_call_log