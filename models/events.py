from pydantic import EmailStr, BaseModel
from typing import List
from models import users as models
from enum import Enum, auto
from datetime import datetime


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class TagEnum(AutoName):
    sporting_events = auto()
    food_events = auto()
    art_expo = auto()
    music_show = auto()


class StatusEnum(AutoName):
    active = auto()
    cancelled = auto()
    ongoing = auto()
    expired = auto()


class Location(BaseModel):
    latitude: float
    longitude: float



# incomplete
# TODO: fix this name to be single event (doesnt make sense for plural)
class Events(BaseModel):
    title: str
    description: str
    date: datetime
    tag: TagEnum
    location: Location
    max_capacity: int
    public: bool
    attending: List[models.Users]
    upvotes: int
    comment_ids: List[str]
    rating: float
    status: StatusEnum
    creator_id: str
    # TODO: add landmark flag OR extend into own class
    # TODO: think about how to handle expiration based on dates


class registration_form(Events):
    pass


class registration_response(BaseModel):
    event_id: str

    
class events_by_location_response(BaseModel):
    events: List[Events]


class get_all_events_by_status_response(BaseModel):
    events: List[Events]
