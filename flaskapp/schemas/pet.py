# encoding: utf-8
import marshmallow as ma


class PetSchema(ma.Schema):
    name = ma.fields.String()


class PetQueryArgsSchema(ma.Schema):
    name = ma.fields.String()
    is_active = ma.fields.Boolean()
