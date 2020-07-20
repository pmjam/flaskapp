# encoding: utf-8
import marshmallow as ma
from .base import BaseSchema


class PetSchema(BaseSchema):
    name = ma.fields.String()


class PetQueryArgsSchema(BaseSchema):
    name = ma.fields.String()
