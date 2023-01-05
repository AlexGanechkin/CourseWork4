from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

genre_ns = Namespace('genres')


# director_schema = MovieSchema()
# director_schema = MovieSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        # movies = movie_service.get_all()
        # return movies_schema.dump(movies), 200
        return "all", 200


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    def get(self, genre_id):
        return "найден", 200
