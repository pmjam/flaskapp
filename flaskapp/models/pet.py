# encoding: utf-8
import mongoengine as me
from .base import BaseDocument


class Pet(BaseDocument):
    name = me.StringField(max_length=60)
