def test_create_table(test_client):
    response = test_client.post("/tables/", json={
        "name": "Table 1",
        "seats": 4,
        "location": "Window"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Table 1"
    assert data["seats"] == 4
