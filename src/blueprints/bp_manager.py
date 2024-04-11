from src.blueprints import v1_blueprints

    # loop blueprintList and register with app
def register_blueprints(app):
    all_blueprints = [
        *v1_blueprints.blueprint_list,  #spread version 1 blueprints
    ]
    
    for blueprint_info in all_blueprints:
        blueprint_instance = blueprint_info['bluePrint']
        blueprint_path = blueprint_info['path']
        app.register_blueprint(blueprint_instance,url_prefix=blueprint_path)
