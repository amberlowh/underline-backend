from config.db import get_database
from fastapi import APIRouter

from models import users as models
from docs import users as docs
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
    "/users/get_user_info",
    response_model=models.get_user_info_response,
    description=docs.get_user_info_desc,
    summary=docs.get_user_info_summ,
    tags=["Users"],
    status_code=200,
)
async def get_user_info(email: str):
    # receive data from client -> util.get_user_info method -> 
    #?return user_id from DB insertion?

    if not email:
        raise HTTPException(status_code=400, detail="Input invalid/not present")

    # get DB instance
    db = get_database()

    # return response in reponse model
    return await util.get_user_info(email)


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

