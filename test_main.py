from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "test"}

def test_update_item(client):
    item_data = {"name": "Product", "price": 9.99, "is_offer": True}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Product", "item_id": 1}

def test_delete_item(client):
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 eliminado"}