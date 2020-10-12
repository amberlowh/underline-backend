from pydantic import EmailStr, BaseModel
from typing import List
from models import users as models

import datetime

# incomplete
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

class events_by_location_response(BaseModel):
    events: List[Events]
