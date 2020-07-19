# encoding: utf-8
from .base import ServiceBase
from flask_login import login_user, logout_user
from flaskapp import models


class ServiceUser(ServiceBase):

    def list(self, **kwargs):
        qs = models.User.objects(**kwargs)
        return qs

    def get(self, id, **kwargs):
        obj = self.list(**kwargs).get(id=id)
        return obj

    def get_by_email(self, email, **kwargs):
        obj = self.list(**kwargs).get(email=email)
        return obj

    def update(self, obj, data):
        item = self.list(id=obj.id).update_one(**data)
        return item

    def delete(self, obj):
        item = self.list(id=obj.id).update_one(is_active=False)
        return item

    def login(self, username, password):
        user = self.get_by_email(username)
        if user.check_password(password):
            login_user(user)
            return True
        else:
            return False

    def logout(self):
        logout_user()
