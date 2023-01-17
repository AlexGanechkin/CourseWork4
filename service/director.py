from dao.director import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_list(self, criteria_list):
        if criteria_list['page'] is not None:
            return self.dao.get_paginated(criteria_list)
        else:
            return self.dao.get_all()

    def get_one(self, entity_id):
        return self.dao.get_one(entity_id)
