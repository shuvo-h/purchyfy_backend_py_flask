
from marshmallow import Schema, fields, validate
from src.errorHandlers.errorMessage import mrslwErrOptions
from sqlalchemy import CheckConstraint

class CatalogueCreateValidationSchema(Schema):
    category_id = fields.Int(required=True,error_messages=mrslwErrOptions('category_id'))
    shop_id = fields.Int(required=True,error_messages=mrslwErrOptions('shop_id'))
    title = fields.Str(required=True,validate=validate.Length(max=100), error_messages=mrslwErrOptions("title", nullable=False))
    price = fields.Int(required=True, error_messages=mrslwErrOptions("price", nullable=False))
    inventory = fields.Int(required=True, error_messages=mrslwErrOptions("inventory", nullable=False))