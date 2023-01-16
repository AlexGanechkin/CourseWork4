
from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthView(Resource):

    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        data = request.json
        access_token = data.get('access_token')
        refresh_token = data.get('refresh_token')

        tokens = auth_service.refresh_tokens(access_token, refresh_token)

        return tokens, 201


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        """ Метод добавляет нового пользователя в базу """
        user_json = request.json

        try:
            user = user_service.create(user_json)
            return "", 201, {'location': f'/users/{user.id}'}
        except Exception as e:
            abort(400)
