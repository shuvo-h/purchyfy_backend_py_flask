from marshmallow import Schema, fields
from src.middlewares import validator_helpers

class RegistrationSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "null": "Email must not be null.",
            "invalid": "Invalid email format.",
            "type": "Email must be a string.",
        },
        validate=validator_helpers.validate_email_def
    )
    password = fields.Str(
        required=True,
        error_messages={
            "required": "Password is required.",
            "invalid": "Password must be a string.",
            "null": "Password must not be null.",
        }
    )
    name = fields.Str(
        required=True,
        error_messages={
            "required": "Name is required.",
            "invalid": "Name must be a string.",
            "null": "Name must not be null.",
        }
    )

class LoginSchema(Schema):
    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required.",
            "null": "Email must not be null.",
            "invalid": "Invalid email format.",
            "type": "Email must be a string.",
        },
        validate=validator_helpers.validate_email_def
    )
    password = fields.Str(
        required=True,
        error_messages={
            "required": "Password is required.",
            "invalid": "Password must be a string.",
            "null": "Password must not be null.",
        }
    )
    
