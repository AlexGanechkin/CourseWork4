from config import Config
from dao.model.director import Director


class DirectorDAO:
    """
        Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
        по таблице director
    """
    def __init__(self, session):
        self.session = session

    def get_paginated(self, criteria_list):
        page = int(criteria_list['page'])
        return self.session.query(Director).paginate(page, Config.RECORDS_PER_PAGE, error_out=False).items

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, entity_id):
        return self.session.query(Director).get(entity_id)

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

        return director

    def delete(self, director):
        self.session.delete(director)
        self.session.commit()
