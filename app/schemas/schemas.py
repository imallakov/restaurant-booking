from pydantic import BaseModel
from datetime import datetime


class TableBase(BaseModel):
    name: str
    seats: int
    location: str


class TableCreate(TableBase):
    pass


class TableRead(TableBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationCreate(ReservationBase):
    pass


class ReservationRead(ReservationBase):
    id: int

    model_config = {
        "from_attributes": True
    }
