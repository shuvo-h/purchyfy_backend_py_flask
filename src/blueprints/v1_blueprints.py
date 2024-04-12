from src.modules import auth,shop,category,catalogue

# arrange all bluprints for version 1 
blueprint_list = [
    {
        "path": f"/api/v1/auth",
        "bluePrint": auth.auth_bp_v1
    },
    {
        "path": f"/api/v1/shops",
        "bluePrint": shop.shop_bp_v1
    },
    {
        "path": f"/api/v1/categories",
        "bluePrint": category.category_bp_v1
    },
    {
        "path": f"/api/v1/catalogues",
        "bluePrint": catalogue.catalogue_bp_v1
    },
]