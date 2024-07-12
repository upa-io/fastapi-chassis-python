from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

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
