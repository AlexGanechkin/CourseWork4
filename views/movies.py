from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    """ Рут получает список фильмов из базы, а также добавляет новый фильм в базу """

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
        return movies_schema.dump(movies), 200

    def post(self):
        """ Метод добавляет новый фильм в базу """
        movie_json = request.json
        movie = movie_service.create(movie_json)
        return "", 201, {'location': f'/movies/{movie.id}'}  # взято с разбора домашки


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id):
        """ Метод получает фильм по его id """
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        """ Метод обновляет фильм в базе """
        json_data = request.json
        json_data['id'] = movie_id
        movie_service.update(json_data)
        return f"Фильм с id - {movie_id} - был обновлен", 204

    def patch(self, movie_id):
        """ Метод частично обновляет фильм в базе """
        self.put(movie_id)
        return "", 204

    def delete(self, movie_id):
        """ Метод удаляет фильм из базы """
        movie_service.delete(movie_id)
        return f"Фильм с id - {movie_id} - был удален из базы", 204
