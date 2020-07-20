# encoding: utf-8
import mongoengine as me
from flaskapp import auth
from .base import BaseDocument


class User(BaseDocument):
    email = me.StringField(max_length=30)
    _password = me.StringField()

    @property
    def password(self):
        try:
            return self._password
        except AttributeError:
            return None

    @password.setter
    def password(self, value):
        self._password = auth.bcrypt.generate_password_hash(value).decode('utf-8')

    def check_password(self, value):
        return auth.bcrypt.check_password_hash(self.password, value) is True

    # flask-login
    # @property
    # def is_active(self):
    #     return True

    @property
    def is_authenticated(self):
        return True

    # @property
    # def is_anonymous(self):
    #     return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')
