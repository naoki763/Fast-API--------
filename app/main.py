from fastapi import FastAPI
from app.routers import users, rooms, booking
from typing import List


app = FastAPI()

app.include_router(users.router)
app.include_router(rooms.router)
app.include_router(booking.router)

