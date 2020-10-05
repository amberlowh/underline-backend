import uuid
from config.db import get_database

DB_NAME = "underline"


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

async def update_item():
