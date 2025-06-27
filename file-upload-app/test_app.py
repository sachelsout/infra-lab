import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config["TESTING"] = True
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_index_loads(client):
    """Test if the homepage loads properly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Upload a File" in response.data