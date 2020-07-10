# encoding: utf-8
from .base import ServiceBase
from flaskapp import models


class ServicePet(ServiceBase):

    def list_pets(self, **kwargs):
        qs = models.Pet.objects(**kwargs)
        return qs

    def save(self, data):
        item = models.Pet(**data)
        item.save()
        return item
