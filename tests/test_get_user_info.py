import time
from fastapi.testclient import TestClient
from app import app
import pytest
import logging

client = TestClient(app)

def check_get_user_response_valid(response, registration data = None):
    valid = True
    valid = valid and response.status_code == 201
    valid = valid and "first_name" in response.json()
    valid = valid and "last_name" in response.json()
    valid = valide and "email" in response.json()
    return valid


# used to test "/users/find"
class TestGetUser:
    def test_get_user_success(self, registered_user):
        # get fake user data to test
        params = {"email": registered_user["email"]}
        # send request to test client
        response = client.get("/users/find", params=params)
        
        # check that response is good
        assert check_get_user_response_valid(response, registered_user)

    def test_get_nonexistent_user_failure(self, registered_user):

        params = {"email": "fake.mail"}
        # send request to test client
        response = client.get("/users/find", params=params)
        # check that response is good
        assert not check_get_user_response_valid(response)
    
    #what other tests, get 

    


