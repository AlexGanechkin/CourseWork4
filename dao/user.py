from sqlalchemy import text

from dao.model.user import User


class UserDAO:
    """
    Функция обращается к БД для получения списка, единичных записей, добавления, удаления, обновления записей
    по таблице user
    """

    def __init__(self, session):
        self.session = session

    def get_one(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user
