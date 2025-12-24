from models import Restaurant,Order
from db import SessionLocal
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID


def getAll(page:int,size:int) -> List[Restaurant]:
    db:Session = SessionLocal()
    restaurants:List[Restaurant] = db.query(Restaurant).offset((page - 1) * size).limit(size).all()
    db.close()
    return restaurants

def addRestaurant(name:str):
    db:Session = SessionLocal()
    new_restaurant = Restaurant(name=name)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    db.close()
    return new_restaurant

def getRestaurantById(restaurant_id: UUID) -> Restaurant:
    db:Session = SessionLocal()
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    db.close()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

