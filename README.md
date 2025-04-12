# 🍽️ Restaurant Table Reservation API

This is a RESTful API service to manage restaurant tables and reservations.

---

## 🚀 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Docker + Docker Compose
- Pytest

---

## 🛠️ How to Run

### 1. Clone and go to directory

```bash
git clone https://github.com/imallakov/restaurant-booking.git
cd restaurant-booking
```

---

### 2. Start app with Docker Compose

```bash
docker-compose up --build
```

📦 Alembic migrations will run automatically on container startup.

---

### 3. Open docs

📚 Swagger UI:

```
http://localhost:8000/docs
```

---

## 📌 First-Time Setup (for developers)

If you're running this project for the first time and no Alembic migrations exist yet:

```bash
docker-compose exec app alembic revision --autogenerate -m "init"
docker-compose exec app alembic upgrade head
```

> ⚠️ This is only needed **once**, to generate the initial database schema.

---

## 🧪 Run Tests

Inside Docker container:

```bash
docker-compose exec app pytest
```

---

## 📂 Project Structure

```
app/
├── main.py
├── models/
├── schemas/
├── services/
├── routers/
├── database.py
alembic/
tests/
entrypoint.sh
```

---

## 📌 Notes

- Table names must be unique (`name` field).
- Reservation validation prevents overlapping times.
- Uses Pydantic V2 and SQLAlchemy 2.

---
