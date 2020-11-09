from starlette.exceptions import HTTPException
from config.db import get_database
from fastapi import APIRouter

from models import events as models
from docs import events as docs
from util import events as utils
import logging

router = APIRouter()

@router.post(
    "/feedback/register",
     response_model=models.registration_form,
    description=docs.registration_desc,
    summary= docs.registration_summ,
    tags["Feedback"],
    status_code=201,
)

async def register_feedback(form: models.registration_form):
    # receive data from client -> util.register ->
    db = get_database()
    feedback_id = await utils.register_feedback(form, db)
    
    return models.registration_response(feedback_id=feedback_id)
        
