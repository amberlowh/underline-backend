# utils/feedback.py
def add_upvote_to_feedback(feedback_id, db):
  collection = db[DB_NAME]["feedback"]
  collection.update_one({"_id": feedback_id}, {"$inc": {"upvotes": 1}})

  