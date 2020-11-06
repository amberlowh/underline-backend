
from config.db import get_database
from fastapi import APIRouter, Response

from models import events as eventModel
from models import feedback as feedbackModel
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
async def delete_feedback(event_id, feedback_id):                   

    # get DB Database
    db = get_database()

    # perform deletion
    await utils.delete_feedback(event_id, feedback_id, db)

    # prevent console error
    return Response(status_code=204) # https://github.com/tiangolo/fastapi/issues/717#issuecomment-583826657
   
@router.post(
    "/feedback/add",
    response_model=feedbackModel.registration_response,
    #description=docs.registration_desc,
    #summary=docs.registration_summ,
    #tags=["Users"],
    status_code=201,
)
async def add_feedback(form: feedbackModel.registration_form):

    # get DB instance
    db = get_database()

    # send the form data and DB instance to util.users.register_user
    feedback_id = await utils.add_feedback(form, db)

    # return response in reponse model
    return feedbackModel.registration_response(feedback_id=feedback_id)