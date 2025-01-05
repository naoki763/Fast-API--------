from fastapi import APIRouter, Depends
from app.schemas.schemas import Booking, BookingCreate
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List
from app.cruds.cruds import get_booking, create_booking


router = APIRouter()


@router.get("/booking", response_model=List[Booking])
async def read_booking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = get_booking(db, skip=skip, limit=limit)
    return bookings

@router.post("/booking", response_model=Booking)
async def create_bookings(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db=db, booking=booking)