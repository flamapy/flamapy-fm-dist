import sys
import pytest
import json

sys.path.append(".")
from app import app

def test_hello_world():
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200


def test_get_plugins():
    # Arrange
    client = app.test_client()

    # Act
    response = client.get(app.config['API_BASE_URL'] + '/info/plugins')
    result = json.loads(response.data)

    # Assert
    assert response.status_code == 200
    assert len(result) > 0


def test_get_operations():
    # Arrange
    client = app.test_client()

    # Act
    response = client.get(app.config['API_BASE_URL'] + '/info/pysat_metamodel/operations')

    # Assert
    assert response.status_code == 308
    response = client.get(response.headers['Location'])

    assert response.status_code == 200
    result = json.loads(response.data)
    assert len(result) > 0
