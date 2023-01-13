from sqlalchemy import text

from dao.model.user import User


class UserDAO:
    """
    Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
    по таблице user
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_by_filter(self, filter_criteria):
        return self.session.query(User).filter(text(filter_criteria))

    def get_one(self, entity_id):
        return self.session.query(User).get(entity_id)

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()
