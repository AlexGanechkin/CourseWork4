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

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        entity_id = data.get('id')

        director = self.get_one(entity_id)

        if 'name' in data:
            director.name = data.get('name')

        self.dao.update(director)

    def delete(self, entity_id):
        director = self.get_one(entity_id)
        self.dao.delete(director)
