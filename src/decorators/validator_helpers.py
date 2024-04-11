from marshmallow import Schema, fields, ValidationError, validate
import re
def validate_email_def(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+(?:\.[a-zA-Z]+)$'
    if not re.match(pattern, email):
        raise ValidationError("Invalid email format.")
    