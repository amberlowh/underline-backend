import uuid
from enum import Enum
from config.db import get_database
from geopy import distance
import logging

DB_NAME = "underline"

async def generate_id():
    return str(uuid.uuid4())

async def register_feedback(form, db):
    
    # cast input form (python class) -> dictionary (become JSON eventually)
    form_dict = form.dict()
     # generating event_id (UUID)
    event_id = await generate_id 
    
    # insert the feedback_id to the dictionary for insertion
    form_dict["_id"] = feedback_id
    
    # create column for insertion in db
    column = db[DB_NAME]["events"]
    
    for key, val in form_dict.items():
            if isinstance(val, Enum):
                form_dict[key] = val.name

    # insert id into column
    column.insert_one(form_dict)

    # return feedback_id if success
    return feedback_id