from pymongo import MongoClient
from config.main import DB_URI
import os


class Database:
    client: MongoClient = None


def is_testing():
    return os.environ.get("_called_from_test") == "True"


def get_db_name():
    return "underline" if not is_testing() else "pytest"


db = Database()


def get_database():
    return db.client


def connect_to_mongo():
    db.client = MongoClient(DB_URI)


def close_connection_to_mongo():
    db.client.close()


def clear_test_collections():
    test_db = db.client["pytest"]
    for collection in test_db.list_collection_names():
        test_db[collection].delete_many({})
