import pytest
from flask import Flask
from app.application import app as flask_app 

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello!"}