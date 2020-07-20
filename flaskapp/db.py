# encoding: utf-8
from flask_mongoengine import MongoEngine
from mongoengine import DoesNotExist

db = MongoEngine()

__all__ = [
    'DoesNotExist',
]
