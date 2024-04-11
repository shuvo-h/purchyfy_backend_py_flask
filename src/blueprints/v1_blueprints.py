from src.modules import auth,shop

# arrange all bluprints for version 1 
blueprint_list = [
    {
        "path": f"/api/v1/auth",
        "bluePrint": auth.auth_bp_v1
    },
    {
        "path": f"/api/v1/marchants",
        "bluePrint": shop.marchat_bp_v1
    },
]