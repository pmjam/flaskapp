# encoding: utf-8
import dateutil


def init_app(app):
    app.add_template_filter(strftime, 'strftime')


def strftime(value, format='%d/%m/%Y %H:%M:%S'):
    if value:
        try:
            return value.strftime(format)
        except AttributeError:
            date = dateutil.parser.parse(value)
            return date.strftime(format)
    else:
        return value
