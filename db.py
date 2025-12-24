import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def init_db():
    from models import Restaurant, Order  # ensure models are registered
   
    Base.metadata.create_all(bind=engine)  # Recreate with current schema


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
