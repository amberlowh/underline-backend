
from config.db import get_database
from fastapi import APIRouter, Response

from models import events as eventModel

#from docs import feedback as docs
import logging
import util.feedback as utils
from starlette.exceptions import HTTPException

router = APIRouter()

@router.delete(
    "/feedback/delete/{event_id}/{feedback_id}",
    #description=docs.delete_user_desc,
    #summary=docs.delete_user_summ,
    #tags=["Users"],
    status_code=204,
)
async def delete_user(event_id, feedback_id):                   

    # get DB Database
    db = get_database()

    # perform deletion
    await utils.delete_feedback(event_id, feedback_id)

    # prevent console error
    return Response(status_code=204) # https://github.com/tiangolo/fastapi/issues/717#issuecomment-583826657
   
    