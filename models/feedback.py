class Feedback(BaseModel):
  comment_text: str
  upvotes: int
  tags: FeedbackTags

class FeedbackTags(Enum):
  GOOD_EVENT = auto()
  ON_TIME = auto()