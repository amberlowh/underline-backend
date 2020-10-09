from starlette.exceptions import HTTPException
from config.db import get_database
from fastapi import APIRouter

from models import events as models
from docs import events as docs
import util.users as utils

router = APIRouter()

@router.post(
    "/events/location/",
    response_model=models.registration_response,
    description=docs.events_by_location_desc,
    summary=docs.events_by_location_summ,
    tags=["Events"],
    status_code=201,
)
async def events_by_location(lat: str, lon: str, radius: int = 10):

    if not lat or not lon:
        raise HTTPException(status_code=400, detail="Missing coordinate(s)")

    db = get_database()

    origin = (lat, lon)

    valid_events = await utils.register_user(origin, radius, db)

    return models.events_by_location_response(events=valid_events)
