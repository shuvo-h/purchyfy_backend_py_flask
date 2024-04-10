from flask_cors import CORS


def configure_cors(app):
    # CORS configuration with whitelisted origins
    CORS(app, origins=['http://localhost:3000', 'http://localhost:3040'])