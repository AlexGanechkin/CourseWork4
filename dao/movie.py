from sqlalchemy import text

from config import Config
from dao.model.movie import Movie


class MovieDAO:
    """
    Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
    по таблице movie
    """
    def __init__(self, session):
        self.session = session

    def get_sorted_paginated(self, criteria_list):
        page = int(criteria_list['page'])
        return self.session.query(Movie).order_by(Movie.year.desc()).\
            paginate(page, Config.RECORDS_PER_PAGE, error_out=False).items

    def get_paginated(self, criteria_list):
        page = int(criteria_list['page'])
        return self.session.query(Movie).paginate(page, Config.RECORDS_PER_PAGE, error_out=False).items

    def get_sorted(self):
        return self.session.query(Movie).order_by(Movie.year.desc())

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, entity_id):
        return self.session.query(Movie).get(entity_id)

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
