# encoding: utf-8
import mongoengine as me
from flask_login import UserMixin
from flaskapp import auth


class User(UserMixin, me.Document):
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
