from config.db import get_database
from geopy import distance
import uuid
import logging

DB_NAME = "underline"


async def generate_id():
    return str(uuid.uuid4())


async def register_event(form, db):
    # cast input form (python class) -> dictionary (become JSON eventually)
    form_dict = form.dict()

    # generating event_id (UUID)
    event_id = await generate_id()

    # insert the event_id to the dictionary for insertion
    form_dict["_id"] = event_id

    # create column for insertion in db
    column = db[DB_NAME]["events"]

    # insert id into column
    column.insert_one(form_dict)

    # return user_id if success
    return event_id


# Returns event dictionary
async def get_event(event_id, db):
    column = db[DB_NAME]["events"]
    user = column.find_one({"_id": event_id})
    return user


async def events_by_location(origin, radius, db):
    def within_radius(event):
        event_location = event.get("location", {})

        event_lat = event_location.get("latitude", 0)
        event_lon = event_location.get("longitude", 0)

        destination = (event_lat, event_lon)

        distance_mi = distance.distance(origin, destination).miles

        return distance_mi <= radius

    column = db[DB_NAME]["events"]

    events = column.find()
    all_events = [event for event in events]

    valid_events = list(filter(within_radius, all_events))

    return valid_events
