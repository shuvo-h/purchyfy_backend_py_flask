from flask import Blueprint, request
from src.decorators.authDecorators import authCheck
from src.decorators.bodyValidator import validate_body
from . import category_controller,category_validator
from src.utils import db_helpers

category_bp = Blueprint('category_v1',__name__)

# create category 
@category_bp.post("/")
@validate_body(category_validator.CategoryCreateValidationSchema())
@authCheck(['admin','user'])
def createCategory(parsedBody):
    return category_controller.create_category(parsedBody)


# get catalogue by category id 
@category_bp.get("/<int:category_id>/catalogues")
@authCheck(['admin', 'user'])  # decorator methods
def getCataloguesByCategoryId(category_id):
    filters = db_helpers.pickToDict(request.args,['searchTerm','title','maxPrice','minPrice','maxInventory','minInventory'])
    paginationInfo = db_helpers.pickToDict(request.args,["page","per_page","sort_order","sort_by"])
    return category_controller.getCataloguesByCategoryId(category_id,filters,paginationInfo)

