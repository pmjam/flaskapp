# encoding: utf-8
from . import pet


def init_app(app):
    app.register_blueprint(pet.mod)
