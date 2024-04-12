from src.utils import catchErrorHandler
from src.utils.sendResFormater import sendRes
from .catalogue_model import CatalogueModel
from src.errorHandlers.appErrorhandler import AppError



# create a catalogue 
@catchErrorHandler.catch_err_handler
def create_catalogue(payload):
    category_id = payload.get('category_id')
    shop_id = payload.get('shop_id')
    title = payload.get('title')
    price = payload.get('price')
    inventory = payload.get('inventory')


    new_catalogue = CatalogueModel(
        category_id=category_id,
        shop_id=shop_id,
        title=title,
        price=price,
        inventory=inventory,
    )
    CatalogueModel.add_and_commit(new_catalogue)
    result = new_catalogue.to_dict()

    return sendRes(201,data=result,message="Catalogue created successfully")