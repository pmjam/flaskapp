# encoding: utf-8
import marshmallow as ma


class TokenSchema(ma.Schema):
    access_token = ma.fields.String()


class LoginArgsSchema(ma.Schema):
    email = ma.fields.String(required=True)
    password = ma.fields.String(required=True)
