from flask import request
from flask_restx import Resource, Namespace, abort

from container import user_service
from dao.model.user import UserSchema

user_ns = Namespace('users')

user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    """ Рут получает список пользователей из базы, а также добавляет нового пользователя в базу """

    def get(self):
        """
        Метод принимает критерии фильтрации базы по роли пользователя и выводит список пользователей,
        соответствующих критериям фильтрации, или весь список если критерии фильтрации не заданы.
        """

        filtration_criteria = request.args.get('role')
        if filtration_criteria is not None:
            filtration_criteria = f"role='{filtration_criteria}'"
        users = user_service.get_list(filtration_criteria)
        return user_schema.dump(users, many=True), 200


@user_ns.route('/<int:user_id>')
class UsersView(Resource):
    def get(self, user_id):
        """ Метод получает пользователя по его id """
        user = user_service.get_one(user_id)
        return user_schema.dump(user), 200

    def put(self, user_id):
        """ Метод обновляет пользователя в базе """
        json_data = request.json
        json_data['id'] = user_id
        user = user_service.update(json_data)
        if user == "Пользователь уже существует":
            abort(400)
        return f"Пользователь с id - {user_id} - был обновлен", 204

    def patch(self, user_id):
        """ Метод частично обновляет пользователя в базе """
        self.put(user_id)
        return "", 204

    def delete(self, user_id):
        """ Метод удаляет пользователя из базы """
        user_service.delete(user_id)
        return f"Пользователь с id - {user_id} - был удален из базы", 204
