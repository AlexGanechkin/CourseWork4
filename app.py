from flask import Flask
from flask_restx import Api

from setup_db import db
from config import Config
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    """ функция создания основного объекта app """
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def register_extensions(application):
    """ функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...) """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    application = create_app(app_config)
    register_extensions(application)

    application.run(host="localhost", port=10001, debug=True)
