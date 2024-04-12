from flask import Blueprint
from src.decorators.authDecorators import authCheck
from src.decorators.bodyValidator import validate_body
from . import catalogue_controller,catalogue_validator

catalogue_bp = Blueprint('catalogue_v1',__name__)

# create catalogue
@catalogue_bp.post("/")
@validate_body(catalogue_validator.CatalogueCreateValidationSchema())
@authCheck(['admin','user'])
def createCatalogue(parsedBody):
    return catalogue_controller.create_catalogue(parsedBody)
