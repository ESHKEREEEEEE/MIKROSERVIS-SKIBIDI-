from typing import Any, Dict, Optional, Union, List
from uuid import UUID

from app.crud.base import CRUDBase
from app.models.request import Request
from app.schemas.request.request import RequestCreate

from sqlalchemy.orm import Session


class CRUDRequest(CRUDBase[Request, RequestCreate, None]):
    def get_list(db: Session, *, skip: int = 0, limit: int = 10):  #
        return db.query(Request).offset(skip).limit(limit).all()  #

    def get_by_sid(self, db: Session, sid: UUID) -> Optional[Request]:  # noqa
        return db.query(Request).filter(Request.sid == sid).first()

request = CRUDRequest(Request)
