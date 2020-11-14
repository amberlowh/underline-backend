import pytest
import os
from config.db import connect_to_mongo, close_connection_to_mongo
from fastapi.testclient import TestClient
from app import app
import datetime
import logging

client = TestClient(app)

# startup process
def pytest_configure(config):
    os.environ['_called_from_test'] = 'True'
    connect_to_mongo()

def pytest_unconfigure(config):
    os.environ['_called_from_test'] = 'False'
    close_connection_to_mongo()

@pytest.fixture(scope='module')
def registered_event_data():
    json = {
        "title": "Test Delete Event (should not have comment)",
        "description": "DIFFERENT TEST DESCRIPTION",
        "date": str(datetime.datetime.now()),
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
    event_response = client.post("/events/register", json=json)
    assert event_response.status_code == 201

    feedback_json = {
        "event_id": event_response.json()["event_id"],
        "comment": "Food tasted good"
    }

    feedback_response = client.post("/feedback/add", json=feedback_json)
    assert feedback_response.status_code == 201

    return {"request": json, "event_response": event_response.json(), "feedback_response": feedback_response.json()}

@pytest.fixture(autouse=True)
def run_around_tests():
    yield