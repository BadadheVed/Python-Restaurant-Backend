from models import Restaurant,Order
from db import SessionLocal
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

def getOrdersByRestaurantId(restaurant_id: UUID, page:int = 1, size:int = 10) -> List[Order]:
    db:Session = SessionLocal()
    orders:List[Order] = db.query(Order).filter(Order.restaurant_id == restaurant_id).offset((page - 1) * size).limit(size).all()
    db.close()
    return orders


def getById(order_id: UUID) -> Order:
    db:Session = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    db.close()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def createOrder(restaurant_id: UUID, name: str) -> Order:
    db:Session = SessionLocal()
    new_order = Order(restaurant_id=restaurant_id, name=name)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()
    return new_order