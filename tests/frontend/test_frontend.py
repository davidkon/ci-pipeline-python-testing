import pytest

from src.app import app as flask_app


class TestFrontendAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        flask_app.config["TESTING"] = True
        self.client = flask_app.test_client()

    def test_index_page(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"Welcome to the Dummy App!" in response.data

    def test_get_items(self):
        response = self.client.get("/api/items")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) >= 2

    def test_get_item_valid(self):
        response = self.client.get("/api/items/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["id"] == 1

    def test_get_item_invalid(self):
        response = self.client.get("/api/items/999")
        assert response.status_code == 404
        data = response.get_json()
        assert "error" in data

    def test_post_item_success(self):
        response = self.client.post("/api/items", json={"name": "New Item"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["name"] == "New Item"
        assert "id" in data

    def test_post_item_missing_name(self):
        response = self.client.post("/api/items", json={})
        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
