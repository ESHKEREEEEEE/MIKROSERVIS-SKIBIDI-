import json
from typing import Generator

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud as crud
from app import models
from app.config.db.session import SessionLocal
from app.config.settigns import settings





def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

