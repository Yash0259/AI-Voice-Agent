from fastapi import APIRouter
from app.controllers.user_controller import create_user,get_users
from app.utils.twilio_service import make_call,send_sms
from app.schemas.user_schema import UserSchema

router  = APIRouter()

@router.post("/users")
def add_user(user:UserSchema):
    return create_user(user)

@router.get("/users")
def list_users():
    return get_users()