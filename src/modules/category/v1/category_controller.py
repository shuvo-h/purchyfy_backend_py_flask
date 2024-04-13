from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .category_model import CategoryModel
from src.errorHandlers.appErrorhandler import AppError

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

