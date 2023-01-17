from flask import request
from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        """ Метод получает список жанров из базы """

        criteria_list = {
            'page': request.args.get('page')
        }
        genres = genre_service.get_list(criteria_list)
        return genre_schema.dump(genres, many=True), 200


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):

    def get(self, genre_id):
        """ Метод получает жанр по его id """

        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
