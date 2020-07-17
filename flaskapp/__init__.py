from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    from flaskapp.db import db
    db.init_app(app)

    from flaskapp import templatefilter
    templatefilter.init_app(app)

    from flaskapp import views
    views.init_app(app)

    from flaskapp.views import rest
    rest.init_app(app)

    return app
