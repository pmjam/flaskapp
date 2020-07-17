# encoding: utf-8
import dateutil


def init_app(app):
    app.add_template_filter(strftime, 'strftime')
    app.add_template_filter(none_to_null, 'none_to_null')


def strftime(value, format='%d/%m/%Y %H:%M:%S'):
    if value:
        try:
            return value.strftime(format)
        except AttributeError:
            date = dateutil.parser.parse(value)
            return date.strftime(format)
    else:
        return value


def none_to_null(value):
    if value:
        return value
    else:
        return ''
