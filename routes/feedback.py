
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
    #description=
    #summary=
    #tags=
    status_code=204,
)
async def delete_event(event_id, feedback_id):                   

    # get DB Database
    db = get_database()

    # perform deletion
    await utils.delete_feedback(event_id, feedback_id, db)

    # prevent console error
    return Response(status_code=204) # https://github.com/tiangolo/fastapi/issues/717#issuecomment-583826657
#does need endpoint
@router.put{
    "/feedback/add-upvote/{feedback_id}}",
    description=docs.add_upvote_desc
    summary=docs.add_upvote_summ
    tags=["Feedback"]
    status_code=200,
}

async def add_upvote_to_feedback(feedback_id):                   

    # get DB Database
    db = get_database()

    # increase upvote count
    await utils.add_upvote_to_feedback(feedback_id, db)

   """
   ??
    return Response(status_code=200) # https://github.com/tiangolo/fastapi/issues/717#issuecomment-583826657
    """


   
    