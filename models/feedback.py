from pydantic import EmailStr, BaseModel
from models import events

class Feedbacks(BaseModel):
    event_id: str
    comment: str

class registration_form(Feedbacks):
    pass

class registration_response(BaseModel):
    feedback_id: str

class get_user_info_response(Feedbacks):
    pass