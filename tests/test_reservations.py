from datetime import datetime, timedelta


def test_create_reservation(test_client):
    response = test_client.post("/tables/", json={
        "name": "Table X",
        "seats": 2,
        "location": "Terrace"
    })
    assert response.status_code == 200
    table_id = response.json()["id"]

    reservation_time = datetime.now().isoformat()
    response = test_client.post("/reservations/", json={
        "customer_name": "Alice",
        "table_id": table_id,
        "reservation_time": reservation_time,
        "duration_minutes": 60
    })

    assert response.status_code == 200


def test_reservation_conflict(test_client):
    response = test_client.post("/tables/", json={
        "name": "Table Y",
        "seats": 2,
        "location": "Window"
    })
    table_id = response.json()["id"]

    reservation_time = datetime.now().isoformat()

    # Бронь на 60 минут
    test_client.post("/reservations/", json={
        "customer_name": "Alice",
        "table_id": table_id,
        "reservation_time": reservation_time,
        "duration_minutes": 60
    })

    # Пересекающаяся бронь
    response = test_client.post("/reservations/", json={
        "customer_name": "Bob",
        "table_id": table_id,
        "reservation_time": reservation_time,
        "duration_minutes": 30
    })

    assert response.status_code == 400
    assert "Table is already reserved" in response.json()["detail"]
