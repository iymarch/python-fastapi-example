from fastapi import FastAPI, Path, Cookie
from starlette.config import Config
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr

app = FastAPI()


