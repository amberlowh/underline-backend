from config.db import get_database


def attempt_login(form, db):
    column = db["underline"]["users"]
    form_dict = form.dict()
    column.insert_one(form_dict)
