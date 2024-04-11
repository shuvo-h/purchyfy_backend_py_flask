from flask import jsonify, request
from marshmallow import ValidationError
from functools import wraps
from src.errorHandlers.appErrorhandler import AppError

def extract_error_messages(errors):
    error_dict = {}
    for field, value in errors.items():
        if isinstance(value, dict):
            error_dict[field] = extract_error_messages(value)
        else:
            error_dict[field] = value[0]
    return error_dict

def validate_body(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = schema.load(request.json)
            except ValidationError as err:
                # print(err)
                err_dict = error_dict = extract_error_messages(err.messages)
                # return jsonify({"errors": err_dict}), 400
                raise AppError(400,"Validation failed",errors=err_dict)
            return func(data, *args, **kwargs)
        return wrapper
    return decorator

