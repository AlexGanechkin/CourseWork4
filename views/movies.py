# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service


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
        return "", 201
