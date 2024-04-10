from os import getenv

envs= {
    'APP_SECRET_KEY': getenv('APP_SECRET_KEY','default_secret_key'),
    'FLASK_ENV': getenv('FLASK_ENV','development'),

    # database config 
    'PG_DB_USERNAME': getenv('PG_DB_USERNAME',None),
    'PG_DB_PASSWORD': getenv('PG_DB_PASSWORD',None),
    'PG_DB_HOST': getenv('PG_DB_HOST'),
    'PG_DB_NAME': getenv('PG_DB_NAME',None),


    # jwt envs 
    'ACCESS_TOKEN_SECRET': getenv('ACCESS_TOKEN_SECRET',None),
    'REFRESH_TOKEN_SECRET': getenv('REFRESH_TOKEN_SECRET',None),
}

