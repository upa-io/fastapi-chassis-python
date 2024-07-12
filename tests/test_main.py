from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_days_between_dates():
    data = {
        "date1": "2023-01-01",
        "date2": "2023-01-31"
    }
    response = client.post("/days_between_dates", json=data)
    assert response.status_code == 200
    assert response.json()["days_between"] == 30

def test_string_to_datetime():
    data = {
        "date_string": "2023-01-01",
        "date_format": "%Y-%m-%d"
    }
    response = client.post("/string_to_datetime", json=data)
    assert response.status_code == 200
    # Asegúrate de que la fecha resultante sea correcta según la lógica de tu aplicación
    assert response.json()["result_date"] == "2023-01-01T00:00:00"

def test_generate_current_datetime():
    response = client.get("/generate_current_datetime")
    assert response.status_code == 200
    assert "current_datetime" in response.json()

def test_get_first_day_of_month():
    # Test the endpoint for getting the first day of a given month
    response = client.get("/first_day_of_month", params={"date": "2023-03-15T00:00:00"})
    assert response.status_code == 200
    assert response.json()["first_day_of_month"] == "2023-03-01T00:00:00"

def test_get_last_day_of_month():
    # Test the endpoint for getting the last day of a given month
    response = client.get("/last_day_of_month", params={"date": "2023-03-15T00:00:00"})
    assert response.status_code == 200
    assert response.json()["last_day_of_month"] == "2023-03-31T00:00:00"
