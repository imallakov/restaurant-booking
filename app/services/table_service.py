from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas


def get_tables(db: Session):
    return db.query(models.Table).all()


def create_table(db: Session, table: schemas.TableCreate):
    db_table = models.Table(**table.model_dump())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_id: int):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if table:
        db.delete(table)
        db.commit()
    return table
