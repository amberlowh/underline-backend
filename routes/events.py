from starlette.exceptions import HTTPException
from config.db import get_database
from fastapi import APIRouter

from models import events as models
from docs import events as docs
import util.users as utils

import logging

router = APIRouter()

#  C - POST
#  R - GET
#  U - PATCH
#  D - DELETE


@router.post(
    "/events/register",
    response_model=models.registration_response,
    tags=["Events"],
    status_code=201,
)
async def register_event(form: models.registration_form):
    # receive data from client -> util.register method -> return user_id from DB insertion

    # get DB instance
    db = get_database()
    # send the form data and DB instance to util.events.register_event
    event_id = await utils.register_event(form, db)

    # return response in reponse model
    return models.registration_response(event_id=event_id)

@router.get(
    "/users/{event_id}",
    response_model=models.Events,
    status_code=201
)
async def get_event(event_id):
    db = get_database()
    event_data = await utils.get_event(event_id, db)
    return models.Events(**event_data)


# FLOW TO CREATE ROUTE(endpoint):
#  1. create model in models/users.py file
#  2. write routing code in routes/users.py file (here)
#  3. implement the actual method handling in utils/users.py file
#  4. write docs in docs/users.py file and test!!

@router.get(
    "/events/location/",
    response_model=models.registration_response,
    description=docs.events_by_location_desc,
    summary=docs.events_by_location_summ,
    tags=["Events"],
    status_code=201,
)
async def events_by_location(lat: str, lon: str, radius: int = 10):

    if not lat or not lon:
        raise HTTPException(status_code=400, detail="Missing coordinate(s)")

    db = get_database()

    origin = (lat, lon)

    valid_events = await utils.register_user(origin, radius, db)

    return models.events_by_location_response(events=valid_events)