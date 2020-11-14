import uuid
from starlette.exceptions import HTTPException
from config.db import get_database
import logging
DB_NAME = "underline"

async def generate_id():
    return str(uuid.uuid4())

# Given an event id and feedback id, attempt to delete the feedback from the event's comment_ids array as well as from the feedback collection
async def delete_feedback(event_id, feedback_id, db):
    
    # Remove feedback from event array
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
    
    # Remove feedback from the feedback collection
    column = db[DB_NAME]["feedback"]
    found_feedback = column.find_one({"_id": feedback_id}) 

    if not found_feedback:
        raise HTTPException(status_code=404,
                            detail="Feedback ID is invalid")

    column.delete_one({"_id": feedback_id})

# Given an event id, create a feedback id and add the feedback to the event
# Event id is a body parameter
async def add_feedback(form, db):
    form_dict = form.dict()
    feedback_id = await generate_id()
    form_dict["_id"] = feedback_id

    event_id = form_dict["event_id"]

    # attempt to find event and add feedback
    column = db[DB_NAME]["events"]
    found_event = column.find_one({"_id": event_id})
    
    if not found_event:
        raise HTTPException(status_code=404,
                            detail="Event ID is invalid")
    
    found_event["comment_ids"].append(feedback_id)
    column.update_one({"_id": event_id}, {"$set": found_event})

    column = db[DB_NAME]["feedback"]
    column.insert_one(form_dict)

    return feedback_id

    #update feedback column some other time

# Returns feedback dictionary
async def get_feedback(feedback_id, db):
    column = db[DB_NAME]["feedback"]
    feedback = column.find_one({"_id": feedback_id})

    if not feedback:
        raise HTTPException(status_code=404,
                            detail="Feedback ID is invalid")

    return feedback
