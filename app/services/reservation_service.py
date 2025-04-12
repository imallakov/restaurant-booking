from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import timedelta

from app.models import models
from app.schemas import schemas
from app.schemas.schemas import ReservationCreate


def get_reservations(db: Session):
    return db.query(models.Reservation).all()


def create_reservation(db: Session, reservation: ReservationCreate):
    end_time = reservation.reservation_time + timedelta(minutes=reservation.duration_minutes)

    conflicting_reservations = db.query(models.Reservation).filter(
        models.Reservation.table_id == reservation.table_id
    ).all()

    for r in conflicting_reservations:
        r_start = r.reservation_time
        r_end = r_start + timedelta(minutes=r.duration_minutes)

        if (reservation.reservation_time < r_end and end_time > r_start):
            raise Exception("Table is already reserved in the given time slot.")

    db_reservation = models.Reservation(**reservation.model_dump())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def delete_reservation(db: Session, reservation_id: int):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == reservation_id).first()
    if reservation:
        db.delete(reservation)
        db.commit()
    return reservation
