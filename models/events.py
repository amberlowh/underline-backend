from pydantic import EmailStr, BaseModel
from typing import List
from models import users as models
from enum import Enum, auto


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


class Event(BaseModel):
    title: str
    description: str
    date: str
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


class registration_form(Event):
    pass


class registration_response(BaseModel):
    event_id: str


class ListOfEvents(BaseModel):
    events: List[Event]


class events_by_location_response(ListOfEvents):
    pass


class get_all_events_by_status_response(ListOfEvents):
    pass


class get_all_events_by_status_response(ListOfEvents):
    pass


class all_events_response(ListOfEvents):
    pass
