from flask import Blueprint
from . import shop_controller
from src.decorators.authDecorators import authCheck
from flask import request
from src.decorators.bodyValidator import validate_body
from . import shop_validator

shop_bp = Blueprint('marchant_v1',__name__)

# create shop 
@shop_bp.post("/")
@validate_body(shop_validator.ShopCreateValidationSchema())
@authCheck(['admin', 'user'])  # decorator methods
def createMarchant(parsedBody):
    return shop_controller.create_shop(request.user['id'],parsedBody)


# get marchant 

# update marchant by id 

# delete(soft) marchant by id 



