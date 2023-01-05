from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

director_ns = Namespace('directors')


# director_schema = MovieSchema()
# director_schema = MovieSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        # movies = movie_service.get_all()
        # return movies_schema.dump(movies), 200
        return "all", 200


@director_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    def get(self, director_id):
        return "найден", 200
