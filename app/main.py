from fastapi import FastAPI
from app.routers import tables, reservations
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Booking API")

app.include_router(tables.router)
app.include_router(reservations.router)
