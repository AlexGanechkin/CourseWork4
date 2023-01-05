from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        movie_json = request.json
        movie_service.create(movie_json)
        return "", 201

@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        json_data = request.json
        json_data['id'] = movie_id
        movie_service.update(json_data)
        return f"Фильм с id - {movie_id} - был обновлен", 204

    def patch(self, movie_id):
        self.put(movie_id)
        return "", 204

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return f"Фильм с id - {movie_id} - был удален из базы", 204
