from flask import jsonify, request
from marshmallow import ValidationError
from functools import wraps
from src.errorHandlers.appErrorhandler import AppError

def validate_body(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                err_dict = {}
                for field, value in err.messages.items():
                    err_dict[field] = value[0] 
                # return jsonify({"errors": err_dict}), 400
                raise AppError(400,"Validation failed",errors=err_dict)
            return func(data, *args, **kwargs)
        return wrapper
    return decorator

