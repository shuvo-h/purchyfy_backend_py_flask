# prevent to generate __pycache__ folder/file in development for each module 
import sys, os
if os.getenv('FLASK_ENV') == 'development':
     sys.dont_write_bytecode = True

from dotenv import load_dotenv;
import os;
from src.app_operator import app_controller
from flask_migrate import Migrate

# load all env variables from .env file
cwd = os.getcwd()
envFilePath=os.path.join(cwd,'.env')
load_dotenv(dotenv_path=envFilePath)

combined_app = app_controller.create_combined_app()

from src.config.db_config import db
migrate = Migrate(combined_app, db)

# combine all app
if __name__ == '__main__':
     # run only one app at a time 
    combined_app.run()