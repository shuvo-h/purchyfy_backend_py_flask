from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .shop_model import ShopModel
from src.modules.order.v1.order_model import OrderModel,ORDER_STATUS
from src.modules.category.v1.category_model import CategoryModel
from sqlalchemy import desc
from src.utils import db_helpers


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



# get order list by shopid 
def getOrdersByShopId(shop_id,filters,pageQuery):
    page, per_page, count, sort_order, sort_by = db_helpers.getPaginationTupple(pageQuery)
    query = OrderModel.query.filter_by(shop_id=shop_id, **filters)

    # Apply sorting dynamically
    # query = query.order_by(getattr(OrderModel, sort_by).asc())
    query = query.order_by(getattr(getattr(OrderModel, sort_by), sort_order)())

    pagination = query.paginate(page=page,per_page=per_page,count=count, error_out=False)
    
    orders = [item.to_dict() for item in pagination.items]
    
    meta = db_helpers.to_meta_dict(pagination,sort_order, sort_by)
    return sendRes(200, data=orders,message="Orders retrived successful!", meta=meta)



# get order list by shopid 
def getCategoriesByShopId(shop_id,filters,pageQuery):
    page, per_page, count, sort_order, sort_by = db_helpers.getPaginationTupple(pageQuery)
    query = CategoryModel.query.filter_by(shop_id=shop_id, **filters)

    # Apply sorting dynamically
    # query = query.order_by(getattr(CategoryModel, sort_by).asc())
    query = query.order_by(getattr(getattr(CategoryModel, sort_by), sort_order)())

    pagination = query.paginate(page=page,per_page=per_page,count=count, error_out=False)
    
    orders = [item.to_dict() for item in pagination.items]
    
    meta = db_helpers.to_meta_dict(pagination,sort_order, sort_by)
    return sendRes(200, data=orders,message="Categories retrived successful!", meta=meta)