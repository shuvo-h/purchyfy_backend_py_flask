from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .category_model import CategoryModel
from src.errorHandlers.appErrorhandler import AppError
from src.utils import db_helpers
from src.modules.catalogue.v1.catalogue_model import CatalogueModel
from src.config import db_config

# create a category 
@catchErrorHandler.catch_err_handler
def create_category(payload):
    shop_id = payload.get('shop_id')
    title = payload.get('title')

    # title is not exist
    existingTitle = CategoryModel.query.filter_by(title=title,shop_id=shop_id).first()
    if existingTitle:
        raise AppError(422,"Title already exist")

    # create a category
    new_category = CategoryModel(shop_id=shop_id,title=title)
    CategoryModel.add_and_commit(new_category)
    result = new_category.to_dict()

    return sendRes(201,data=result,message="Category created successfully")


# get order list by shopid 
def getCataloguesByCategoryId(category_id,filters,pageQuery):
    page, per_page, count, sort_order, sort_by = db_helpers.getPaginationTupple(pageQuery)
    
     # Extract searchTerm if available
    searchTerm = filters.pop('searchTerm', None)

    # take out special fields(sequence is important)
    rangeQueryFields = ["minPrice","maxPrice","minInventory","maxInventory"]
    [minPrice, maxPrice,minInventory,maxInventory],restFilters = db_helpers.dictToPositionalList(filters,rangeQueryFields)

    # conditional filtering
    filter_conditions = []

    # Add category_id filter
    filter_conditions.append(getattr(CatalogueModel, "category_id") == category_id)

    if maxPrice is not None:
        filter_conditions.append(getattr(CatalogueModel,"price") <= maxPrice)
    if minPrice is not None:
        filter_conditions.append(getattr(CatalogueModel,"price") >= minPrice)

    if maxInventory is not None:
        filter_conditions.append(getattr(CatalogueModel,"inventory") <= maxInventory)
    if minInventory is not None:
        filter_conditions.append(getattr(CatalogueModel,"inventory") >= minInventory)
    
    # Integrate remaining filters from restFilters
    for key, value in restFilters.items():
        filter_conditions.append(getattr(CatalogueModel, key) == value)

    # Apply regex search if searchTerm is provided
    if searchTerm:
        regex_conditions = []
        for field in ["title",]:
            regex_conditions.append(getattr(CatalogueModel, field).ilike(f"%{searchTerm}%"))
        filter_conditions.append(db_config.db.or_(*regex_conditions))

   
     # Start with an unrestricted query
    query = CatalogueModel.query

     # Apply all filter conditions
    if filter_conditions:
        query = query.filter(*filter_conditions)
    

    # Apply sorting dynamically
    # query = query.order_by(getattr(OrderModel, sort_by).asc())
    query = query.order_by(getattr(getattr(CatalogueModel, sort_by), sort_order)())

    pagination = query.paginate(page=page,per_page=per_page,count=count, error_out=False)
    
    catalogues = [item.to_dict() for item in pagination.items]
    
    meta = db_helpers.to_meta_dict(pagination,sort_order, sort_by)
    return sendRes(200, data=catalogues,message="Catalogues retrived successful!", meta=meta)


