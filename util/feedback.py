import uuid
from starlette.exceptions import HTTPException
from config.db import get_database
import logging

DB_NAME = "underline"


# Given an event id and feedback id, attempt to delete the feedback from the event's comment_ids array
async def delete_feedback(event_id, feedback_id, db):
    column = db[DB_NAME]["events"]

    found_event = column.find_one({"_id": event_id})

    if not found_event:
        raise HTTPException(status_code=404,
                            detail="Event ID is invalid")

    if feedback_id in found_event["comment_ids"]:
        found_event["comment_ids"].remove(feedback_id)
    else:
        raise HTTPException(status_code=404,
                            detail="Feedback ID not found in the provided event")

    column.update_one({"_id": event_id}, {"$set": found_event})


# Returns event dictionary
async def get_feedback(feedback_id, db):
    column = db[DB_NAME]["feedback"]
    user = column.find_one({"_id": feedback_id})
    return user
