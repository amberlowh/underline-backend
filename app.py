from fastapi.middleware.cors import CORSMiddleware
from config.db import connect_to_mongo, close_connection_to_mongo
from config.main import app
from routes.users import router as users_router
from routes.events import router as events_router
from routes.feedback import router as feedback_router

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}


origins = [
    "https://localhost",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "https://sparkdev-underline.herokuapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(events_router)
app.include_router(feedback_router)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_connection_to_mongo)
