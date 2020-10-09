from config.db import get_database
from geopy import distance

DB_NAME = "underline"

async def events_by_location(origin, radius, db):

    def within_radius(event):
        event_location = event.get("location")

        event_lat = event_location.get("latitude", "0") 
        event_lon = event_location.get("longitude", "0")
 
        destination = (event_lat, event_lon)

        distance = distance.distance(origin, destination).miles

        return distance <= radius

    column = db[DB_NAME]["events"]

    events = column.find({}, {"_id":0, "location":1})

    valid_events = map(within_radius, events)

    return valid_events
