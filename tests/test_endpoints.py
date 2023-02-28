import sys
sys.path.append("..")

from app import app
import pytest
import json



def test_hello_world():
    client = app.test_client()

    response = client.get(app.config['API_BASE_URL'])
    assert response.status_code == 200


