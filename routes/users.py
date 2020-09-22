from config.db import get_database
from fastapi import APIRouter

from models.login import login_description, login_summary, LoginForm, LoginResponse
import util.users as utils

router = APIRouter()


@router.post(
    "/login",
    response_model=LoginResponse,
    description=login_description,
    summary=login_summary,
    tags=["Users"],
    status_code=200,
)
def login(form: LoginForm):
    db = get_database()
    utils.attempt_login(form, db)
    return {"success": True}
