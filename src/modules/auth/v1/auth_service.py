from flask import jsonify
from src.errorHandlers.appErrorhandler import AppError
from src.modules.users.v1.user_model import UserModel,UserRole
from ....utils import jwt_helpers
from src.config.env_config import envs
from src.config.db_config import db

def registerUserIntoDb(payload):
    # extract all data
    email = payload.get('email')
    password = payload.get('password')
    name = payload.get('name')
        
    # check if user already exist
    existUser = UserModel.query.filter_by(email=email).first()
    if existUser: 
        # Roll back the transaction
        raise AppError(422,"User already exist")

    # create a new user
    new_user = UserModel(
        email=email,
        password=password,
        name=name,
        role= 'user'
    )
    UserModel.set_password(new_user,password)
    UserModel.add_and_commit(new_user=new_user)

    # create jwt and cookies
    token_payload = {
        'id': new_user.id,
        'email': new_user.email,
        'role': new_user.role
    }
    access_token = jwt_helpers.generate_token(token_payload,envs['ACCESS_TOKEN_SECRET'])
    refresh_token = jwt_helpers.generate_token(token_payload,envs['REFRESH_TOKEN_SECRET'],expiration_time=6*30*24*60*60)

    # create response
    response = jsonify({
        'success': True,
        'message':"Registration successful",
        'data': {
            'access_token': access_token,
            'user': {
                'id': new_user.id,
                'email': email,
                'role': new_user.role,
                'name': new_user.name,
            }
        }
    })
    response.status_code = 201

    # Set HTTP-only cookies for access token and refresh token
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=2 * 30 * 24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )

    return response



def loginUserFromDb(payload):
    email = payload.get('email')
    password = payload.get('password')

    # if user exist
    existUser = UserModel.query.filter_by(email=email).first()
    if not existUser:
        raise AppError(404,"User not found!")
    
    # match password
    if not UserModel.check_password(existUser.password,password):
        raise AppError(404,"Password didn't match!")
    
    # generate tokens
    token_payload = {
        "id": existUser.id,
        "email": existUser.email,
        "name": existUser.name,
        "role": existUser.role,
    }
    access_token = jwt_helpers.generate_token(token_payload,envs['ACCESS_TOKEN_SECRET'])
    refresh_token = jwt_helpers.generate_token(token_payload,envs['REFRESH_TOKEN_SECRET'],expiration_time=6*30*24*60*60)

 
    response = jsonify({
        'success': True,
        'message':"Login successful",
        'data': {
            "token": access_token,
            "user": token_payload
        }
    })
    response.status_code = 200

    # Set HTTP-only cookies for access token and refresh token
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=2 * 30 * 24 * 60 * 60,
        path="/",
        secure=True,
        httponly=True
    )

    return response