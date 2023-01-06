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
