# encoding: utf-8
from flask_smorest import Api
from . import pet
from . import auth


def init_app(app):
    api = Api(app)
    api.register_blueprint(pet.mod, url_prefix='/api/pets')
    api.register_blueprint(auth.mod, url_prefix='/api/auth')
