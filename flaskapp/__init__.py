from flask import Flask
from flask_smorest import Api


def create_app():
    app = Flask(__name__)
    app.config['API_TITLE'] = 'My API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.2'
    app.config["OPENAPI_URL_PREFIX"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
    app.config['MONGODB_SETTINGS'] = {
        'db': 'dbflaskapp',
        'host': 'localhost',
        'port': 27017,
        'username': 'test',
        'password': ''
    }
    from flaskapp.db import db
    db.init_app(app)

    from flaskapp.views import pet
    api = Api(app)
    api.register_blueprint(pet.mod)
    return app
