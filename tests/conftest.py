import pytest
import os
from config.db import connect_to_mongo, close_connection_to_mongo
from fastapi.testclient import TestClient
from datetime import datetime

from app import app

client = TestClient(app)


# startup process
def pytest_configure(config):
    os.environ['_called_from_test'] = 'True'
    connect_to_mongo()


def pytest_unconfigure(config):
    os.environ['_called_from_test'] = 'False'
    close_connection_to_mongo()


@pytest.fixture(scope='module')
def registered_user():
    user_data = {
        "first_name": "Testing_first",
        "last_name": "Testing_last",
        "email": "test@mail.com"
    }
    response = client.post("/users/register", json=user_data)
    return user_data


@pytest.fixture(scope='module')
def registered_event():
    event_data = {"lat": "75", "lon": "50", "radius": 20}
    response = client.get("/events/register", json=event_data)
    return response


@pytest.fixture(scope='module')
def events_locations():
    location_data = {"lat": "75", "lon": "50", "radius": 20}
    response = client.get("/events/location/", params=location_data)
    return response


@pytest.fixture(autouse=True)
def run_around_tests():
    yield


@pytest.fixture(scope='module')
def registered_event_data():
    json = {
        "title": "Test Event",
        "description": "Test event",
        "date": str(datetime.now()),
        "tag": "sporting_events",
        "location": {
            "latitude": 75.0,
            "longitude": 75.0
        },
        "max_capacity": 10,
        "public": False,
        "attending": [],
        "upvotes": 0,
        "comment_ids": [],
        "rating": 5.0,
        "status": "active",
        "creator_id": "0"
    }
    response = client.post("/events/register", json=json)
    assert response.status_code == 201
    return json
