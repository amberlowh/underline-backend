import uuid
from starlette.exceptions import HTTPException
from config.db import get_database
import logging
from config.db import DB_NAME


async def generate_id():
    return str(uuid.uuid4())


async def register_user(form, db):
    # cast input form (python class) -> dictionary (become JSON eventually)
    form_dict = form.dict()

    # generating user_id (UUID)
    user_id = await generate_id()

    # insert the user_id to the dictionary for insertion
    form_dict["_id"] = user_id

    # create column for insertion in db
    column = db[DB_NAME]["users"]

    # insert id into column
    column.insert_one(form_dict)

    # return user_id if success
    return user_id


#method handling GET
#what exactly is the client getting, the user info,
#firstname last and email


async def get_user_info(email, db):
    #why is it email, db ... commas?
    column = db[DB_NAME]["users"]

    #make query from identifier input
    query = {"email": email}

    #query to database
    response = column.find_one(query)

    if not response:
        raise HTTPException(status_code=404, detail="User does not exist")

    return response


async def delete_user(email, db):

    # create column for insertion in db
    column = db[DB_NAME]["users"]

    response = column.delete_one({"email": email})
    if response.deleted_count == 0:
        raise HTTPException(status_code=404,
                            detail="User not found and could not be deleted")


# Returns user dictionary
async def get_user(user_id, db):
    column = db[DB_NAME]["users"]
    user = column.find_one({"_id": user_id})
    return user
