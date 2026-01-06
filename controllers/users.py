import hashlib
import bcrypt
from controllers.jwt import create_access_token
from fastapi import HTTPException
from sqlalchemy.orm import Session

from db import SessionLocal
from models.user import User


# ---------- password helpers ----------

def _pre_hash(password: str) -> bytes:
    """
    Convert password to SHA256 hash (32 bytes) to ensure it's under bcrypt's 72-byte limit.
    """
    return hashlib.sha256(password.encode("utf-8")).digest()


def hash_password(password: str) -> str:
   
    pre_hashed = _pre_hash(password)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pre_hashed, salt)
    return hashed.decode('utf-8')  


def verify_password(password: str, hashed_password: str) -> bool:
   
    pre_hashed = _pre_hash(password)
    return bcrypt.checkpw(pre_hashed, hashed_password.encode('utf-8'))



def signup(email: str, password: str) -> User:
    db: Session = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        new_user = User(
            email=email,
            hashed_password=hash_password(password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()


def login(email: str, password: str) -> tuple[str, User]:
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == email).first()

        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "email": user.email
            }
        )

        return access_token, user
    finally:
        db.close()