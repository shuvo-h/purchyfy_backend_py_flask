from marshmallow import Schema, fields, validate
from src.errorHandlers.errorMessage import mrslwErrOptions

class LocationSchema(Schema):
    lat = fields.Float(required=True, error_messages=mrslwErrOptions("longitude", nullable=False))
    lang = fields.Float(required=True, error_messages=mrslwErrOptions("longitude", nullable=False))

class AddressSchema(Schema):
    road = fields.Str( required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("road", nullable=False))
    city = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("city", nullable=False))
    state = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("state", nullable=False))
    country = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("country", nullable=False))
    post = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("post", nullable=False))
    location = fields.Nested(LocationSchema,required=True, error_messages=mrslwErrOptions("location", nullable=False))

class ShopCreateValidationSchema(Schema):
    shop_name = fields.Str(
        required=True, 
        validate=validate.Length(max=100), 
        error_messages=mrslwErrOptions("shop_name", nullable=False)
    )
    address = fields.Nested(AddressSchema,required=True,error_messages=mrslwErrOptions("address", nullable=False))