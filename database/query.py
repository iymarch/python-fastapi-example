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