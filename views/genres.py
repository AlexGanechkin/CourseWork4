from flask import request
from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema
from helpers.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """ Метод получает список жанров из базы """

        criteria_list = {
            'page': request.args.get('page')
        }
        genres = genre_service.get_list(criteria_list)
        return genre_schema.dump(genres, many=True), 200

    @admin_required
    def post(self):
        """ Метод добавляет новый жанр в базу """
        genre_json = request.json
        genre = genre_service.create(genre_json)
        return "", 201, {'location': f'/directors/{genre.id}'}


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    @auth_required
    def get(self, genre_id):
        """ Метод получает жанр по его id """

        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, genre_id):
        """ Метод обновляет жанр в базе """
        json_data = request.json
        json_data['id'] = genre_id
        genre_service.update(json_data)
        return f"Режиссер с id - {genre_id} - был обновлен", 204

    @admin_required
    def delete(self, genre_id):
        """ Метод удаляет жанр из базы """
        genre_service.delete(genre_id)
        return f"Режисер с id - {genre_id} - был удален из базы", 204
