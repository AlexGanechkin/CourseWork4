# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, entity_id):
        return self.dao.get_one(entity_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        entity_id = data.get('id')

        movie = self.get_one(entity_id)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        # movie.genre_id = data.get('genre_id')
        # movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, entity_id):
        movie = self.get_one(entity_id)
        self.dao.delete(movie)
