from fastapi import FastAPI
from db import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}


print("Database initialized")