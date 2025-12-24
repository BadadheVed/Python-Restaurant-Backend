from enum import Enum

from sqlalchemy import Column, String, ForeignKey, text, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    restaurant_id = Column(
        UUID(as_uuid=True),
        ForeignKey("restaurant.id"),
        nullable=False
    )
    name = Column(String, nullable=False)

    status = Column(
        SQLEnum(OrderStatus, name="order_status"),
        nullable=False,
        default=OrderStatus.PENDING
    )

    restaurant = relationship(
        "Restaurant",
        back_populates="orders"
    )
