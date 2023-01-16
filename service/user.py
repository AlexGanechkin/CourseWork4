import base64
import hashlib
import hmac

from flask_restx import abort

from constants import HASH_SALT, HASH_ITERATIONS, HASH_ALGO
from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_list(self, filtration_request=None):
        """
        Метод получает полный список пользователей, имеющийся в базе, либо список, отфильтрованный по роли
        """

        if filtration_request is not None:
            return self.dao.get_by_filter(filtration_request)
        else:
            return self.dao.get_all()

    def get_one(self, entity_id):
        """ Метод получает пользователя по его id """
        return self.dao.get_one(entity_id)

    def create(self, data):
        """ Метод добавляет нового пользователя в базу, проверка на уникальность email """

        email = data['email']
        password = data['password']

        if None in [email, password]:
            raise Exception

        data['password'] = self.get_hash(password)
        return self.dao.create(data)

    def update(self, data):
        """ Метод обновляет пользователя в базе - все поля или часть из них, в зависимости от полученных данных """
        entity_id = data.get('id')

        user = self.get_one(entity_id)

        if 'username' in data:
            if self.dao.get_by_filter(f"username='{data['username']}'").count() > 0:
                return "Пользователь уже существует"
            user.username = data.get('username')
        if 'password' in data:
            user_password = data.get('password')
            user.password = self.get_hash(user_password)
        if 'role' in data:
            user.role = data.get('role')

        self.dao.update(user)

    def delete(self, entity_id):
        """ Метод удаляет пользователя из базы """
        try:
            user = self.get_one(entity_id)
            self.dao.delete(user)
        except Exception as e:
            abort(400)

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
