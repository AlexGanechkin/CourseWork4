from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        """
        Метод получает список всех фильмов либо постраничный список фильмов,
        отсортированный по году создания в порядке убывания.
        параметр page задает какую страницу выводить
        параметр status определяет нужно ли сортировать список
        """

        criteria_list = {
            'status': request.args.get('status'),
            'page': request.args.get('page')
        }
        movies = movie_service.get_list(criteria_list)
        return movie_schema.dump(movies, many=True), 200


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):

    def get(self, movie_id):
        """ Метод получает фильм по его id """
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200
