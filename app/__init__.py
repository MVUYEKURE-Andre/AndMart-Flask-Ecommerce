from flask import Flask
from config import Config

from .extensions import db, login_manager, migrate, csrf


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)


    # initialize extensions

    db.init_app(app)

    login_manager.init_app(app)
    # login_manager.login_view = "main.login"

    migrate.init_app(app, db)

    csrf.init_app(app)


    # register routes

    from .routes import main

    app.register_blueprint(main)


    return app


from .models import User


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))