import uuid
from config.db import get_database
from starlette.exceptions import HTTPException

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


async def update_user(user_id, new_data, db):
    col = db[DB_NAME]["users"]

    # check that the user exists
    user_query = {"_id": user_id}
    old_data = col.find_one(user_query)
    if not old_data:
        raise HTTPException(status_code=404, detail="User not found")

    # update the dict then insert new data into DB
    old_data.update(new_data)
    col.update_one(user_query, {"$set": old_data})

    # return updated data dict
    return old_data
