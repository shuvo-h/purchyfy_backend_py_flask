from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .shop_model import ShopModel
from src.modules.order.v1.order_model import OrderModel,ORDER_STATUS
from src.modules.category.v1.category_model import CategoryModel
from sqlalchemy import desc
from src.utils import db_helpers
from src.config import db_config


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




# get shops list 
def getShops(queries,paginationInfo):
    page, per_page, count, sort_order, sort_by = db_helpers.getPaginationTupple(paginationInfo)
    
     # Extract searchTerm if available
    searchTerm = queries.pop('searchTerm', None)
    # take out special fields(sequence is important)
    rangeQueryFields = []
    [],restQueries = db_helpers.dictToPositionalList(queries,rangeQueryFields)

    # conditional filtering
    filter_conditions = []

     # Integrate remaining filters from restFilters
    for key, value in restQueries.items():
        filter_conditions.append(getattr(ShopModel, key) == value)

    # Apply regex search if searchTerm is provided
    if searchTerm:
        print(searchTerm)
        regex_conditions = []
        for field in ["shop_name",]:
            regex_conditions.append(getattr(ShopModel, field).ilike(f"%{searchTerm}%"))

        # For JSON field (address is a JSON field)
        for field in ["road", "city", "post", "state", "country"]:
            regex_conditions.append(ShopModel.address.op('->>')(field).ilike(f"%{searchTerm}%"))

        # regex_conditions.append(ShopModel.address.op('->>')('road').ilike(f"%{searchTerm}%"))
        # regex_conditions.append(ShopModel.address.op('->>')('city').ilike(f"%{searchTerm}%"))
        # regex_conditions.append(ShopModel.address.op('->>')('post').ilike(f"%{searchTerm}%"))
        # regex_conditions.append(ShopModel.address.op('->>')('state').ilike(f"%{searchTerm}%"))
        # regex_conditions.append(ShopModel.address.op('->>')('country').ilike(f"%{searchTerm}%"))

        filter_conditions.append(db_config.db.or_(*regex_conditions))

     # Start with an unrestricted query
    query = ShopModel.query

     # Apply all filter conditions
    if filter_conditions:
        query = query.filter(*filter_conditions)

    # Apply sorting dynamically
    # query = query.order_by(getattr(OrderModel, sort_by).asc())
    query = query.order_by(getattr(getattr(ShopModel, sort_by), sort_order)())

    pagination = query.paginate(page=page,per_page=per_page,count=count, error_out=False)
    
    shops = [item.to_dict() for item in pagination.items]
    
    meta = db_helpers.to_meta_dict(pagination,sort_order, sort_by)
    return sendRes(200, data=shops,message="Shops are retrived successful!", meta=meta)


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