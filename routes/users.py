from config.db import get_database
from fastapi import APIRouter

from models import users as models
from docs import users as docs
import logging
import util.users as utils

router = APIRouter()

#  C - POST
#  R - GET
#  U - PATCH
#  D - DELETE


@router.post(
    "/users/register",
    response_model=models.registration_response,
    description=docs.registration_desc,
    summary=docs.registration_summ,
    tags=["Users"],
    status_code=201,
)
async def register_user(form: models.registration_form):
    # receive data from client -> util.register method -> return user_id from DB insertion

    # get DB instance
    db = get_database()
    # send the form data and DB instance to util.users.register_user
    user_id = await utils.register_user(form, db)

    # return response in reponse model
    return models.registration_response(user_id=user_id)

@router.get(
    "/users/{user_id}",
    response_model=models.Users,
    status_code=201
)

async def get_user(user_id):
    db = get_database()
    user_data = await utils.get_user(user_id, db)    
    return models.Users(**user_data)


# FLOW TO CREATE ROUTE(endpoint):
#  1. create model in models/users.py file
#  2. write routing code in routes/users.py file (here)
#  3. implement the actual method handling in utils/users.py file
#  4. write docs in docs/users.py file and test!!


#  delete user - @eduardo

#  get user data - @danny

#  update user - @clement

#  login - @lazaro
#  - implement bcrypt ON the model class
