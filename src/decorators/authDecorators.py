
from src.utils import jwt_helpers
from functools import wraps
from flask import request
from src.config.env_config import envs
from src.errorHandlers.appErrorhandler import AppError
from src.modules.users.v1.user_model import UserModel

# Reusable decorator method for authentication check
def authCheck(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if cookies exist
            if 'access_token' not in request.cookies:
                raise AppError(401,"Unauthorized",{'access_oken':'Access token is required'})

            # Verify JWT token
            token = request.cookies.get('access_token')
            payload = jwt_helpers.verify_jwt_token(token, envs['ACCESS_TOKEN_SECRET'])

            # Check if token is valid
            if payload:
                # Check if user role is allowed
                if payload.get('role') in roles:

                    # check if use is real user
                    existUser = UserModel.query.filter_by(id=payload.get('id'))
                    if not existUser:
                        raise AppError(401,"User desn't exist",{'role':"Couldn't find the user"})

                    # Add decoded user to the request
                    request.user = payload
                    return func(*args, **kwargs)
                else:
                    
                    raise AppError(401,"Not permitted role",{'role':'You are not permitted to acces this resource'})
            else:
                raise AppError(401,"Invalid token",{'role':'Invalid access token is not accepted'})
        return wrapper
    return decorator
