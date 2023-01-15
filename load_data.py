import json

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.model.user import User
from setup_db import db


def read_json():
    with open('fixtures.json', encoding="utf-8") as f:
        data = json.load(f)

    movies = data['movies']
    genres = data['genres']
    directors = data['directors']

    for movie in movies:
        movie_obj = Movie(title=movie['title'], description=movie['description'], trailer=movie['trailer'],
                          year=movie['year'], rating=movie['rating'], genre_id=movie['genre_id'],
                          director_id=movie['director_id'])
        db.session.add(movie_obj)
        db.session.commit()

    for genre in genres:
        genre.pop('pk')
        genre_obj = Genre()
        for k, p in genre.items():
            setattr(genre_obj, k, p)
        db.session.add(genre_obj)
        db.session.commit()

    for director in directors:
        director_obj = Director(name=director['name'])
        db.session.add(director_obj)
        db.session.commit()

    """ Создаем одного пользователя из json для теста
    users = data['users']

    for user in users:
        user_obj = User()
        for k, p in user.items():
            setattr(user_obj, k, p)
        db.session.add(user_obj)
        db.session.commit()
    """
