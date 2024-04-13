from flask import Blueprint
from src.decorators.authDecorators import authCheck
from src.decorators.bodyValidator import validate_body
from . import category_controller,category_validator

category_bp = Blueprint('category_v1',__name__)

# create category 
@category_bp.post("/")
@validate_body(category_validator.CategoryCreateValidationSchema())
@authCheck(['admin','user'])
def createCategory(parsedBody):
    return category_controller.create_category(parsedBody)
