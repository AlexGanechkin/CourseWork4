from flask import request
from flask_restx import Resource, Namespace, abort

from container import user_service
from dao.model.user import UserSchema
from helpers.decorators import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    """ Рут получает пользователя из базы, обновляет данные по нему (в т.ч. пароль) """

    @auth_required
    def get(self, email=None):
        """ Метод получает данные пользователя по email, который по-умолчанию извлекается из токена """

        if email is None:
            abort(400)

        user = user_service.get_user(email)
        return user_schema.dump(user), 200

    @auth_required
    def patch(self, email=None):
        """ Метод обновляет пользователя (имя, фамилия,любимый жанр) в базе. Поиск осуществляется по email """

        data = request.json
        data['email'] = email
        user_service.update(data)
        return "", 201


@user_ns.route('/password')
class UsersView(Resource):

    @auth_required
    def put(self, email=None):
        data = request.json
        data['email'] = email
        user_service.update_password(data)
        return "", 201
