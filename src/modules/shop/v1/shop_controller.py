from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .shop_model import ShopModel


# create a shop
@catchErrorHandler.catch_err_handler
def create_shop(user_id,payload):
    # extract all data
    shop_name = payload.get('shop_name')
    address = payload.get('address')
    print(user_id,shop_name,address)

    newShop = ShopModel(
        user_id=user_id,
        shop_name=shop_name,
        address=address
    )
    ShopModel.add_and_commit(newShop)

    result = ShopModel.to_dict(newShop)
    return sendRes(201, data=result,message="Shop created successful!")