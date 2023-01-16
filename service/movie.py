from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_list(self, criteria_list):
        """
        Метод получает полный список фильмов, имеющийся в базе, либо список, отфильтрованный по режиссеру и/или
        жанру фильма и/или году создания (в зависимости от полученных параметров в словаре).
        """

        if criteria_list['status'] == "new" and criteria_list['page'] is not None:
            return self.dao.get_sorted_paginated(criteria_list)
        elif criteria_list['status'] == "new":
            return self.dao.get_sorted()
        elif criteria_list['page'] is not None:
            return self.dao.get_paginated(criteria_list)
        else:
            return self.dao.get_all()

    def get_one(self, entity_id):
        """ Метод получает фильм по его id """
        return self.dao.get_one(entity_id)

    def create(self, data):
        """ Метод добавляет новый фильм в базу """
        return self.dao.create(data)

    def update(self, data):
        """ Метод обновляет фильм в базе - все поля или часть из них, в зависимости от полученных данных """
        entity_id = data.get('id')

        movie = self.get_one(entity_id)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)

    def delete(self, entity_id):
        """ Метод удаляет фильм из базы """
        movie = self.get_one(entity_id)
        self.dao.delete(movie)
