from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    success: bool


login_description = "Logs in user with username and password. Return success boolean"
login_summary = "Login Endpoint"
