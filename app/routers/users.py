from fastapi import APIRouter, Depends
from app.schemas.schemas import Users, UsersCreate
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.cruds.cruds import get_users, create_user


router = APIRouter()

@router.get("/users", response_model=List[Users])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users", response_model=Users)
async def create_users(user: UsersCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
