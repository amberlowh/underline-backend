from fastapi import FastAPI
from config.db import connect_to_mongo, close_connection_to_mongo
from routes.users import router as users_router


app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


app.include_router(users_router)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_connection_to_mongo)
