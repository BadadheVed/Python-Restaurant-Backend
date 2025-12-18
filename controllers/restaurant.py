from models import Restaurant,Order
from db import SessionLocal
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List


def getAll(page:int,size:int):
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