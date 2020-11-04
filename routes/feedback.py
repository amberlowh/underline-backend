from config.db import get_database
from fastapi import APIRouter, Response
from models import events as eventModel
# from docs import feedback as docs
import logging
import util.feedback as utils
from util import events as utilss

from starlette.exceptions import HTTPException

router = APIRouter()


@router.delete(
    "/feedback/delete/{event_id}/{feedback_id}",
    # description=
    # summary=
    # tags=
    status_code=204,
)
async def delete_event(event_id, feedback_id):
    # get DB Database
    db = get_database()

    # perform deletion
    await utils.delete_feedback(event_id, feedback_id, db)

    # prevent console error
    return Response(status_code=204)  # https://github.com/tiangolo/fastapi/issues/717#issuecomment-583826657


@router.get("/users/{feedback}", response_model=eventModel.Events, status_code=201)
async def get_feedback(feedback_id):
    db = get_database()
    feedback_data = await utilss.get_feedback(feedback_id, db)
    return eventModel.Events(**feedback_data)
