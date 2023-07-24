import unittest
from fastapi.testclient import TestClient
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_read_item(self):
        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": None})

        response = self.client.get("/items/1?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": "test"})

    def test_update_item(self):
        item_data = {"name": "Product", "price": 9.99, "is_offer": True}
        response = self.client.put("/items/1", json=item_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_name": "Product", "item_id": 1})

    def test_delete_item(self):
        response = self.client.delete("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Item 1 eliminado"})


if __name__ == "__main__":
    unittest.main()