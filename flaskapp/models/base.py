# encoding: utf-8
import mongoengine as me
import datetime


class BaseDocument(me.DynamicDocument):
    created_at = me.DateTimeField(default=datetime.datetime.now)
    updated_at = me.DateTimeField()
    is_active = me.BooleanField(default=True)
    meta = {
        'abstract': True,
    }
