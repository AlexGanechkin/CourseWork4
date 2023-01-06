from sqlalchemy import text

from dao.model.movie import Movie


class MovieDAO:
    """
    Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
    по таблице movie
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_filter(self, filter_criteria):
        return self.session.query(Movie).filter(text(filter_criteria))

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
