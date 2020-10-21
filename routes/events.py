from config.db import get_database
from fastapi import APIRouter

from models import events as models
#from docs import events as docs
from docs import events as docs
import logging
import util.events as utils

router = APIRouter()

#  C - POST
#  R - GET
#  U - PATCH
#  D - DELETE


@router.post(
    "/events/register",
    response_model=models.registration_response,
    description=docs.registration_desc,
    summary=docs.registration_summ,
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