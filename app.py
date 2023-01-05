from flask import Flask
from flask_restx import Api

from models import Review, Book
from setup_db import db
from views.books import book_ns
from views.reviews import review_ns
from config import Config


def create_app(config_object):
    """ функция создания основного объекта app """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """ функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...) """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=10001, debug=True)
