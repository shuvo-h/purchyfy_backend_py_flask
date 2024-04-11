from flask import Blueprint,jsonify, request
from . import auth_controller
from src.decorators.bodyValidator import validate_body
from . import auth_validator


auth_bp = Blueprint("auth_v1",__name__)

# register a new user
@auth_bp.post("/register")
@validate_body(auth_validator.RegistrationSchema())
def regester_user_route(validBodyData):
    # bodyData = request.get_json()
    return auth_controller.register_userCtl(validBodyData)

# login a user
@auth_bp.post("/login")
@validate_body(auth_validator.LoginSchema())
def login_user_route(validBodyData):
    # body = request.get_json()
    return auth_controller.login_userCtl(validBodyData)