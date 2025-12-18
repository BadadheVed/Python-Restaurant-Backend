from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base


class Restaurant(Base):
    __tablename__="restaurant"
    id = Column(UUID,primary_key=True,server_default=text("gen_random_uuid()"))
    name = Column(String , nullable=False) 
    orders = relationship(
        "Order",
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )