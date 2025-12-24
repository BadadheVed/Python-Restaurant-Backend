from fastapi import FastAPI
from db import init_db
from routers.router import router as restaurant_router
from routers.orders import router as orders_router
app = FastAPI()
app.include_router(restaurant_router)
app.include_router(orders_router)
@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}


print("Database initialized")