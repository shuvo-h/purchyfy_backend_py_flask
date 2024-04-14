from flask import Blueprint, request
from . import shop_controller
from src.decorators.authDecorators import authCheck
from src.decorators.bodyValidator import validate_body
from . import shop_validator
from src.utils import db_helpers

shop_bp = Blueprint('marchant_v1',__name__)

# create shop 
@shop_bp.post("/")
@validate_body(shop_validator.ShopCreateValidationSchema())
@authCheck(['admin', 'user'])  # decorator methods
def createShop(parsedBody):
    return shop_controller.create_shop(request.user['id'],parsedBody)

# get shops 
@shop_bp.get("/")
@authCheck(['admin', 'user'])  # decorator methods
def getShops():
    queries = db_helpers.pickToDict(request.args,['searchTerm','shop_name','address'])
    paginationInfo = db_helpers.pickToDict(request.args,["page","per_page","sort_order","sort_by"])
    return shop_controller.getShops(queries,paginationInfo)


# get orders by shop_id 
@shop_bp.get("/<int:shop_id>/orders")
@authCheck(['admin', 'user'])  # decorator methods
def getOrdersByShop_id(shop_id):
    # print(request.args)
    filters = db_helpers.pickToDict(request.args,['status'])
    paginationInfo = db_helpers.pickToDict(request.args,["page","per_page","sort_order","sort_by"])
    return shop_controller.getOrdersByShopId(shop_id,filters,paginationInfo)

# get orders by shop_id 
@shop_bp.get("/<int:shop_id>/categories")
@authCheck(['admin', 'user'])  # decorator methods
def getCategoriesByShop_id(shop_id):
    # print(request.args)
    filters = db_helpers.pickToDict(request.args,[])
    paginationInfo = db_helpers.pickToDict(request.args,["page","per_page","sort_order","sort_by"])
    return shop_controller.getCategoriesByShopId(shop_id,filters,paginationInfo)





# get marchant 

# update marchant by id 

# delete(soft) marchant by id 



