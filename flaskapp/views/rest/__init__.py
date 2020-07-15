# encoding: utf-8
from flask_smorest import Api
from . import pet


def init_app(app):
    api = Api(app)
    api.register_blueprint(pet.mod)
