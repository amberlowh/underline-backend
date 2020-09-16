from fastapi import FastAPI

from models.login import login_description, login_summary, LoginForm, LoginResponse

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.post(
    "/login",
    response_model=LoginResponse,
    description=login_description,
    summary=login_summary,
    tags=["Users"],
    status_code=200,
)
def login(form: LoginForm):
    return {"success": True}
