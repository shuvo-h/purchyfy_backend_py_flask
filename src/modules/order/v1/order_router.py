from flask import Blueprint
from src.decorators.authDecorators import authCheck
from src.decorators.bodyValidator import validate_body
from . import order_controller,order_validation


order_bp = Blueprint("order_v1",__name__)

# create order 
@order_bp.post("/")
@validate_body(order_validation.OrderCreateValidationSchema())
@authCheck(['admin','user'])
def createCatalogue(parsedBody):
    return order_controller.create_order(parsedBody)