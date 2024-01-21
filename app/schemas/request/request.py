from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID
import re

from app.schemas.core import CoreModel


class Params(CoreModel):
    param1: str
    param2: int


class RequestBase(CoreModel):
    # sid: Optional[str]
    name: Optional[str]
    params: Optional[Params]

    class Config:
        orm_mode = True


class RequestCreate(RequestBase):
    # sid: UUID
    name: str
    params: Params


class Request(RequestBase):
    sid: UUID
    name: str
    params: Params


class RequestUpdate(RequestBase):
    name: Optional[str]
    params: Optional[dict]
