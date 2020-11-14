import time
from fastapi.testclient import TestClient
from app import app
import pytest
import logging

client = TestClient(app)

class TestDeleteFeedback:
    def test_delete_feedback_success(self, registered_event_data):
        # Get event and feedback ids from the fixture
        event_id = registered_event_data["event_response"]["event_id"]
        feedback_id = registered_event_data["feedback_response"]["feedback_id"]

        # Check if feedback exists and that it's registered to the event id from the fixture
        response = client.get("/feedback/" + feedback_id)
        assert response.status_code == 201
        assert response.json()["event_id"] == event_id

        # Delete it and ensure the deletion goes through
        response = client.delete("/feedback/delete/" + event_id + "/" + feedback_id)
        assert response.status_code == 204 # don't think it's ever not 204 anyway

        # Attempt to get the deleted feedback, should fail
        response = client.get("/feedback/" + feedback_id)
        assert response.status_code == 404

