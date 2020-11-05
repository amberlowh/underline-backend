import time
from fastapi.testclient import TestClient
from app import app
import pytest
import logging

client = TestClient(app)


def check_delete_user_response_valid(response):
    valid = True
    valid = valid and response.status_code == 204
    valid = valid and not response.json()
    return valid


# used to test "/users/delete"
class TestDeleteUser:
    def test_delete_user_success(self):
        # send request to check if client is deleted
        response = client.delete("/users/delete")
        # check that response is good
        assert check_delete_user_response_valid(response)

    def test_register_user_empty_data_failure(self):
        # send request to test client
        response = client.post("/users/delete", json={})
        # check that response is good
        assert not check_delete_user_response_valid(response)
