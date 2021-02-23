from fastapi import FastAPI
from starlette.config import Config


from routers import contact, call_log
from database import SessionLocal, engine
from models import db


db.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(contact.router)
app.include_router(call_log.router)
