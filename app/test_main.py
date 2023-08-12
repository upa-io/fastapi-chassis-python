from fastapi.testclient import TestClient
from .main import app, Item
import pytest

items = []

@pytest.fixture
def client():
    return TestClient(app)

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item(client):
    response = client.get("/items/1?q=test")

    assert response.status_code == 200
    item_id = int(response.json()["item_id"])

    assert item_id == 1
    assert response.json()["q"] == "test"

    response = client.get("/items/2")

    assert response.status_code == 200
    item_id = int(response.json()["item_id"])

    assert item_id == 2
    assert response.json()["q"] is None

def test_update_item(client):
    item_data = {"name": "Product", "price": 9.99, "is_offer": True}
    response = client.put("/items/1", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"item_name": "Product", "item_id": 1}

def test_delete_item(client):
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 eliminado"}

def test_create_item(client):
    item_data = {"name": "Item1", "price": 9.99, "is_offer": True}
    response = client.post("/items/", json=item_data)

    assert response.status_code == 201

def test_get_options():
    with TestClient(app) as client:
        response = client.options("/items/")

    assert response.status_code == 200

    assert response.json() == {"message": "OPTIONS response"}

def test_partial_update_item(client):
    initial_item = Item(name="InitialItem", price=10.0)
    items.append(initial_item)
    
    item_id = 0
    item_data = {"name": "UpdatedItem", "price": 15.0}

    response = client.patch(f"/items/{item_id}", json=item_data)
    
    assert response.status_code == 200

def test_update_item_invalid_item_id(client):
    item_data = {"name": "Product", "price": 9.99, "is_offer": True}
    response = client.put("/items/invalid_id", json=item_data)
    assert response.status_code == 422

def test_delete_item_invalid_item_id(client):
    response = client.delete("/items/invalid_id")
    assert response.status_code == 422
    