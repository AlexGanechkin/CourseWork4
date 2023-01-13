from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema
from helpers.decorators import auth_required, admin_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    """ Рут получает список фильмов из базы, а также добавляет новый фильм в базу """

    @auth_required
    def get(self):
        """
        Метод принимает критерии фильтрации базы (id режиссера и/или жанра и/или год создания)
        и выводит список фильмов, соответствующих критериям фильтрации, или весь список если критерии фильтрации не
        заданы.
        """

        criteria_list = {
            'director_id': request.args.get('director_id'),
            'genre_id': request.args.get('genre_id'),
            'year': request.args.get('year')
        }
        movies = movie_service.get_list(criteria_list)
        return movie_schema.dump(movies, many=True), 200

    @admin_required
    def post(self):
        """ Метод добавляет новый фильм в базу """
        movie_json = request.json
        movie = movie_service.create(movie_json)
        return "", 201, {'location': f'/movies/{movie.id}'}  # взято с разбора домашки


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    @auth_required
    def get(self, movie_id):
        """ Метод получает фильм по его id """
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, movie_id):
        """ Метод обновляет фильм в базе """
        json_data = request.json
        json_data['id'] = movie_id
        movie_service.update(json_data)
        return f"Фильм с id - {movie_id} - был обновлен", 204

    @admin_required
    def patch(self, movie_id):
        """ Метод частично обновляет фильм в базе """
        self.put(movie_id)
        return "", 204

    @admin_required
    def delete(self, movie_id):
        """ Метод удаляет фильм из базы """
        movie_service.delete(movie_id)
        return f"Фильм с id - {movie_id} - был удален из базы", 204
