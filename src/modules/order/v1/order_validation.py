
from marshmallow import Schema, fields, validate
from src.errorHandlers.errorMessage import mrslwErrOptions
from sqlalchemy import CheckConstraint

class ContactSchema(Schema):
    name = fields.Str(
        required=True,
        validate=validate.Length(max=100), 
        error_messages=mrslwErrOptions("name", nullable=False))
    phone = fields.Str(
        required=True,
        validate=validate.Regexp(r'^\+\d{1,3}\d{6,14}$', error="Invalid phone number format."),
        error_messages=mrslwErrOptions("phone", nullable=False)
    )


class OrderItemSchema(Schema):
    catalogue_id = fields.Int(
        required=True,
        error_messages=mrslwErrOptions("catalogue_id", nullable=False)
    )
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0.01),
        error_messages=mrslwErrOptions("price", nullable=False)
    )
    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1),
        error_messages=mrslwErrOptions("quantity", nullable=False)
    )

class OrderCreateValidationSchema(Schema):
    shop_id = fields.Int(
        required=True,
        error_messages=mrslwErrOptions('shop_id', nullable=False)
    )
    total_price = fields.Float(
        required=True,
        validate=validate.Range(min=0.01),
        error_messages=mrslwErrOptions("total_price", nullable=False)
    )
    order_items = fields.List(
        fields.Nested(OrderItemSchema),
        required=True,
        validate=validate.Length(min=1),
        error_messages=mrslwErrOptions("order_items", nullable=False)
    )
    contact = fields.Nested(
        ContactSchema,
        required=True,
        error_messages=mrslwErrOptions("contact", nullable=False)
    )
