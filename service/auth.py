import calendar
import datetime

import jwt
from flask_restx import abort

from constants import SECRET, TOKEN_ALGO, ACCESS_TOKEN_LIFE, REFRESH_TOKEN_LIFE
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_list(f"username='{username}'")[0]

        if user is None:
            raise abort(404)

        if not is_refresh:
            user_password_hash = self.user_service.get_hash(password)
            if not self.user_service.compare_passwords(user.password, user_password_hash):
                abort(400)

        user_data = {'username': user.username, 'role': user.role}
        access_token = self.get_token(user_data, ACCESS_TOKEN_LIFE)
        refresh_token = self.get_token(user_data, REFRESH_TOKEN_LIFE)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def refresh_tokens(self, user_refresh_token):
        user_data = {}
        if user_refresh_token is None:
            abort(401)

        try:
            user_data = jwt.decode(jwt=user_refresh_token, key=SECRET, algorithms=[TOKEN_ALGO])
        except Exception as e:
            abort(401)

        if calendar.timegm(datetime.datetime.utcnow().timetuple()) - user_data['exp'] > REFRESH_TOKEN_LIFE:
            abort(401)

        tokens = self.generate_tokens(user_data['username'], None, True)

        return tokens

    def get_token(self, user_data, token_life):
        token_life = datetime.datetime.utcnow() + datetime.timedelta(minutes=token_life)
        user_data['exp'] = calendar.timegm(token_life.timetuple())
        user_token = jwt.encode(user_data, SECRET, TOKEN_ALGO)
        return user_token
