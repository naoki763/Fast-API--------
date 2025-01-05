from sqlalchemy.orm import Session
from app.models.models import Users as MU, Rooms as MR, Booking as MB
from app.schemas.schemas import Users, Rooms, Booking, UsersCreate, RoomsCreate, BookingCreate
from fastapi import HTTPException


# ユーザ一覧取得
## skip: 上位のデータをスキップするかどうか
## limit: 100件まで取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    ## offset: skipする項目
    ## limit
    return db.query(MU).offset(skip).limit(limit).all()

# 会議室一覧取得
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MR).offset(skip).limit(limit).all()

# 予約一覧取得
def get_booking(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MB).offset(skip).limit(limit).all()

# ユーザ登録
def create_user(db: Session, user: UsersCreate):
    db_user = MU(user_name=user.user_name)
    db.add(db_user)
    db.commit()
    # 反映後にリフレッシュ
    db.refresh(db_user)
    return db_user

# 部屋登録
def create_room(db: Session, room: RoomsCreate):
    db_room = MR(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 予約登録
def create_booking(db: Session, booking : BookingCreate):
    db_booked = db.query(MB).\
        filter(MB.room_id == booking.room_id).\
        filter(MB.end_datetime > booking.start_datetime).\
        filter(MB.start_datetime < booking.end_datetime).\
        all()
    
    # 重複する予約がなければ
    if len(db_booked) == 0:
        db_booking = MB(
        user_id=booking.user_id,
        room_id=booking.room_id,
        booked_num=booking.booked_num,
        start_datetime=booking.start_datetime,
        end_datetime=booking.end_datetime
        )
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    else:
        raise HTTPException(status_code=404, detail="Already booked !")
    