from dao.genre import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, entity_id):
        return self.dao.get_one(entity_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        entity_id = data.get('id')

        genre = self.get_one(entity_id)

        if 'name' in data:
            genre.name = data.get('name')

        self.dao.update(genre)

    def delete(self, entity_id):
        genre = self.get_one(entity_id)
        self.dao.delete(genre)
