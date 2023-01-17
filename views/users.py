from flask import request
from flask_restx import Resource, Namespace

from container import user_service
from dao.model.user import UserSchema
from helpers.decorators import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    """ Рут получает список пользователей из базы, а также добавляет нового пользователя в базу """

    @auth_required
    def get(self, email=None):
        """
        Метод принимает критерии фильтрации базы по роли пользователя и выводит список пользователей,
        соответствующих критериям фильтрации, или весь список если критерии фильтрации не заданы.
        """

        data = request.args.to_dict()
        if email is not None:
            data['email'] = email

        users = user_service.get_user(data)

        if 'email' in data:
            return user_schema.dump(users), 200
        else:
            return user_schema.dump(users, many=True), 200

    @auth_required
    def patch(self, email=None):
        """ Метод обновляет пользователя (имя, фамилия,любимый жанр) в базе. Поис осуществляется по id, email """

        data = request.json
        data['email'] = email
        user_service.update(data)
        return "", 201

    @auth_required
    def put(self, email=None):
        data = request.json
        data['email'] = email
        user_service.update_password(data)
        return "", 201
