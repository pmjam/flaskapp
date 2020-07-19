# encoding: utf-8
from flaskapp.services import ServiceUser
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


bcrypt = Bcrypt()
login_manager = LoginManager()
service = ServiceUser()


def init_app(app):
    bcrypt.init_app(app)
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return service.get(user_id)
