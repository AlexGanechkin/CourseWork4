from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_list(self, criteria_list):
        """ Метод получает полный список фильмов, имеющийся в базе, либо отсортированный список """

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
