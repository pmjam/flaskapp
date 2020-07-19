# encoding: utf-8
from . import pet
from . import login


def init_app(app):
    app.register_blueprint(login.mod)
    app.register_blueprint(pet.mod, url_prefix='/pets')
