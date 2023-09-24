import pytest
import requests
from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    return app.test_client()

def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Add id client in route to have his data' in response.data

def test_get_id_client_route(client):
    """Test the get_id_client route."""
    response = client.get('/123')  # Replace '123' with a valid client ID
    assert response.status_code == 200
    assert b'The id is 123' in response.data

def test_get_model_route(client):
    """Test the get_model route."""
    response = client.get('/get-model')
    assert response.status_code == 200
