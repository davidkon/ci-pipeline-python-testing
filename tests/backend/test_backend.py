import pytest
from src.app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Dummy App!" in response.data

def test_get_all_items(client):
    response = client.get('/api/items')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2  # Initial dummy items

def test_get_single_item_success(client):
    response = client.get('/api/items/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "name" in data

def test_get_single_item_not_found(client):
    response = client.get('/api/items/999')
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data

def test_add_item_success(client):
    new_item = {"name": "Item Three"}
    response = client.post('/api/items', json=new_item)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Item Three"
    assert "id" in data

def test_add_item_missing_name(client):
    response = client.post('/api/items', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
