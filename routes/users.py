from config.db import get_database
from fastapi import APIRouter

from models.login import login_description, login_summary, LoginForm, LoginResponse

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
    return {"success": True}
