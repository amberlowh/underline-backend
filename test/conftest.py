import pytest
import os
from config.db import connect_to_mongo, close_connection_to_mongo
from fastapi.testclient import TestClient
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


@pytest.fixture(autouse=True)
def run_around_tests():
    yield