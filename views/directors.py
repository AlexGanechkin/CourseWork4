from flask import request
from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required

director_ns = Namespace('directors')


director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """ Метод получает список режиссеров из базы """

        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200

    @admin_required
    def post(self):
        """ Метод добавляет нового режиссера в базу """
        director_json = request.json
        director = director_service.create(director_json)
        return "", 201, {'location': f'/directors/{director.id}'}


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    @auth_required
    def get(self, director_id):
        """ Метод получает режиссера по его id """

        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, director_id):
        """ Метод обновляет режиссера в базе """
        json_data = request.json
        json_data['id'] = director_id
        director_service.update(json_data)
        return f"Режиссер с id - {director_id} - был обновлен", 204

    @admin_required
    def delete(self, director_id):
        """ Метод удаляет режиссера из базы """
        director_service.delete(director_id)
        return f"Режисер с id - {director_id} - был удален из базы", 204
