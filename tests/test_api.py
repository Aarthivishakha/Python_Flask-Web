import json
import unittest
from uuid import uuid4

from app import create_app


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def post_json(self, path, payload):
        return self.client.post(
            path, data=json.dumps(payload), content_type="application/json"
        )

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_item_crud(self):
        response = self.post_json("/api/v1/items", {"name": "Keyboard", "price": 99.5})
        self.assertEqual(response.status_code, 201)
        item = json.loads(response.data)
        path = "/api/v1/items/" + item["id"]
        self.assertEqual(self.client.get(path).status_code, 200)
        self.assertEqual(self.client.delete(path).status_code, 204)
        self.assertEqual(self.client.get(path).status_code, 404)

    def test_validation(self):
        response = self.post_json("/api/v1/items", {"name": "", "price": -1})
        self.assertEqual(response.status_code, 400)

    def test_missing_item(self):
        response = self.client.get("/api/v1/items/" + str(uuid4()))
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
