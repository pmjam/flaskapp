# encoding: utf-8
from flaskapp.services import ServiceUser
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager


bcrypt = Bcrypt()
jwt = JWTManager()
service = ServiceUser()
login_manager = LoginManager()
login_manager.login_view = 'login.signin'


def init_app(app):
    bcrypt.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return service.get(user_id)
