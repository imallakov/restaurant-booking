from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import schemas
from app.services import reservation_service

router = APIRouter(prefix="/reservations", tags=["reservations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.ReservationRead])
def read_reservations(db: Session = Depends(get_db)):
    return reservation_service.get_reservations(db)


@router.post("/", response_model=schemas.ReservationRead)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    try:
        return reservation_service.create_reservation(db, reservation)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return reservation_service.delete_reservation(db, reservation_id)
