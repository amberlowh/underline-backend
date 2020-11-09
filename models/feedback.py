class Feedback(BaseModel):
    comment_text: str
    upvotes: int
    tags: FeedbackTags
    
class FeedbackTags(Enum):
    GOOD_EVENT = auto()
    ON_TIME()

class Feedback_form(Feedback):
    pass
class Feedback_response(BaseModel):
    Feedback_id:str
    
def add_upvote_to_feedback(feedback_id, db):
    pass
