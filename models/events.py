from pydantic import EmailStr, BaseModel
from typing import List
from models import users as models
from enum import Enum

import datetime


# incomplete
# TODO: fix this name to be single event (doesnt make sense for plural)
class Events(BaseModel):
    title: str
    #description: str
    #date: datetime
    #tag: TagEnum
    #location: Location
    #max_capacity: int
    #public: bool
    #attending: List[models.Users]
    #upvotes: int
    #comment_ids: List[str]
    #rating: float
    #status: StatusEnum
    #creator_id: str
    # TODO: add landmark flag OR extend into own class
    # TODO: think about how to handle expiration based on dates


class registration_form(Events):
    pass


class registration_response(BaseModel):
    event_id: str


class get_all_events_by_status_response(BaseModel):
    events: List[Events]
