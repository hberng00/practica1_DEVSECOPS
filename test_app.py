import pytest
from app import app

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200  # Check if the status code is 200
    assert response.data == b"Hello, CI/CD with Docker!"  # Check if the content matches
