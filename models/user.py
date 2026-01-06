from enum import Enum

from sqlalchemy import Column, String, ForeignKey, text, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    orders = relationship(
        "Order",
        back_populates="user"
    )