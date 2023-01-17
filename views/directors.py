from flask import request
from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema

director_ns = Namespace('directors')


director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """ Метод получает список режиссеров из базы """

        criteria_list = {
            'page': request.args.get('page')
        }
        directors = director_service.get_list(criteria_list)
        return director_schema.dump(directors, many=True), 200


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):

    def get(self, director_id):
        """ Метод получает режиссера по его id """

        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200
