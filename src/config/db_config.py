from flask_sqlalchemy import SQLAlchemy
from .env_config import envs


# intitiate database 
db = SQLAlchemy()

# configure database
def connectDb(app):
    # Configure the database URIs:   'mysql://username:password@localhost/db_name'
    # when postgreAQL = f'postgresql://username:password@localhost/dbname'
    # when mysql = f'mysql://username:password@localhost/db_name'
    # when sqLite = f'sqlite:///path/to/database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{envs['PG_DB_USERNAME']}:{envs['PG_DB_PASSWORD']}@{envs['PG_DB_HOST']}/{envs['PG_DB_NAME']}"

    
    # Suppress deprecation warnings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Check for stale connections
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True} 

    # Initialize SQLAlchemy with the Flask application
    db.init_app(app)


    # Create all database tables
    with app.app_context():
        db.create_all()




