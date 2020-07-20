# encoding: utf-8
import marshmallow as ma


class BaseSchema(ma.Schema):
    created_at = ma.fields.DateTime()
    updated_at = ma.fields.DateTime()
    is_active = ma.fields.Boolean()
