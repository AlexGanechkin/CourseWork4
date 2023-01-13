from dao.model.genre import Genre


class GenreDAO:
    """
        Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
        по таблице genre
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, entity_id):
        return self.session.query(Genre).get(entity_id)

    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

        return genre

    def delete(self, genre):
        self.session.delete(genre)
        self.session.commit()
