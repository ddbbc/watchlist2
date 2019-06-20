from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.settings')

    db.init_app(app)

    register(app)

    return app


def register(app):
    from .home import home
    from .login import login
    from .errors import error
    app.register_blueprint(home)
    app.register_blueprint(login)
    app.register_blueprint(error)
