from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import schemas
from app.services import table_service

router = APIRouter(prefix="/tables", tags=["tables"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.TableRead])
def read_tables(db: Session = Depends(get_db)):
    return table_service.get_tables(db)


@router.post("/", response_model=schemas.TableRead)
def create_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
    return table_service.create_table(db, table)


@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    return table_service.delete_table(db, table_id)
