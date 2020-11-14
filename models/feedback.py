from pydantic import EmailStr, BaseModel
from models import events


class Feedback(BaseModel):
    event_id: str
    comment: str


class registration_form(Feedback):
    pass


class registration_response(BaseModel):
    feedback_id: str
