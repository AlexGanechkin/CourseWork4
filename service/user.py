import base64
import hashlib
import hmac

from flask_restx import abort

from constants import HASH_SALT, HASH_ITERATIONS, HASH_ALGO
from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user(self, email):
        """ Метод получает пользователя по email """

        return self.dao.get_one(email)

    def create(self, data):
        """ Метод добавляет нового пользователя в базу, проверка на уникальность email """

        email = data['email']
        password = data['password']

        if None in [email, password]:
            raise Exception
        elif password == '' or email == '':
            raise Exception

        data['password'] = self.get_hash(password)
        return self.dao.create(data)

    def update(self, data):
        """
        Метод обновляет пользователя в базе - все поля или часть из них, в зависимости от полученных данных
        Поиск пользователя осуществляется по email.
        """

        user = self.dao.get_one(data['email'])

        if user is None:
            abort(404)

        for k, v in data.items():
            setattr(user, k, v)

        self.dao.update(user)

    def update_password(self, data):
        """ Метод обновляет пароль пользователя, проводится валидация старого пароля. """

        user = self.dao.get_one(data['email'])

        if user is None:
            abort(400)

        old_password = self.get_hash(data['password_1'])

        if not self.compare_passwords(user.password, old_password):
            abort(400)

        new_password = self.get_hash(data['password_2'])
        data = {'email': user.email, 'password': new_password}
        self.update(data)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            HASH_ALGO,
            password.encode('utf-8'),
            HASH_SALT,
            HASH_ITERATIONS
        )).decode('utf-8', 'ignore')

    def compare_passwords(self, database_password, user_password):
        return hmac.compare_digest(
            base64.b64decode(database_password),
            base64.b64decode(user_password)
        )
