import os

DB_URI = os.environ.get("MONGO_DB_URI")
if not DB_URI:
    raise Exception("Key Error: DB_URI not set!")
