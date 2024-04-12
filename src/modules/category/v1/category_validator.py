from marshmallow import Schema, fields, validate
from src.errorHandlers.errorMessage import mrslwErrOptions

class CategoryCreateValidationSchema(Schema):
    shop_id = fields.Int(required=True,error_messages=mrslwErrOptions('shop_id'))
    title = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("title", nullable=False))