# utils/feedback.py
def add_upvote_to_feedback(feedback_id, db):
  collection = db[DB_NAME]["feedback"]
  collection.update_one({"_id": feedback_id}, {"$inc": {"upvotes": 1}})

  #ADD UPVOTE TO FEEDBACKyou dont need to do models

=======
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
>>>>>>> 129f9504e497a3f699d2dbfa17ea518c13b72321
  