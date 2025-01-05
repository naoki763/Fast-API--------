from fastapi import APIRouter, Depends
from app.schemas.schemas import Rooms, RoomsCreate
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.cruds.cruds import get_rooms, create_room


router = APIRouter()


@router.get("/rooms", response_model=List[Rooms])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = get_rooms(db, skip=skip, limit=limit)
    return rooms

@router.post("/rooms", response_model=Rooms)
async def create_rooms(room: RoomsCreate, db: Session = Depends(get_db)):
    return create_room(db=db, room=room)