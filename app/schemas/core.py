import uuid
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """

    pass


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class SIDModelMixin(DateTimeModelMixin):
    sid: Optional[UUID] = uuid.uuid4().hex
