# encoding: utf-8
from .base import ServiceBase
from flaskapp import models


class ServicePet(ServiceBase):

    def list(self, **kwargs):
        qs = models.Pet.objects(**kwargs)
        return qs

    def get(self, slug, **kwargs):
        obj = self.list(**kwargs).get(id=slug)
        return obj

    def create(self, data):
        item = models.Pet(**data)
        item.save()
        return item

    def update(self, obj, data):
        item = self.list(id=obj.id).update_one(**data)
        return item

    def delete(self, obj):
        item = self.list(id=obj.id).update_one(is_active=False)
        return item
