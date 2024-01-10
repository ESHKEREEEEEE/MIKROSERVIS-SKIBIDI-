import sqlalchemy
import uuid

from app.config.db.base_tablename_class import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, VARCHAR, JSON

REQUEST_SCHEMA = "request"

metadata = sqlalchemy.MetaData()


class Request(Base):
    def __init__(self, name: str, params: dict):
        self.sid = uuid.uuid4()
        self.name = name
        self.params = params

    __tablename__ = "requests"
    __table_args__ = {"schema": REQUEST_SCHEMA}


    sid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        primary_key=True,
        index=True,
        default=lambda: uuid.UUID(),
    )
    name = Column(
        VARCHAR(length=100), nullable=False, comment="name of person"
    )
    params = Column(JSON(), nullable=False, comment="params of request")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"sid={self.sid}, "
            f"name={self.name}, "
            f"params={self.params})>"
        )


