from pymongo import MongoClient
from config.main import DB_URI
import os


class Database:
    client: MongoClient = None


def is_testing():
    return os.environ.get("_called_from_test") == "True"


DB_NAME = "underline" if not is_testing() else "pytest"

db = Database()


def get_database():
    return db.client


def connect_to_mongo():
    db.client = MongoClient(DB_URI)


def close_connection_to_mongo():
    db.client.close()
