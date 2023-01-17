import jwt
from flask import request
from flask_restx import abort

from constants import TOKEN_ALGO, SECRET


def auth_required(func):

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            user = jwt.decode(token, SECRET, algorithms=[TOKEN_ALGO])
            email = user.get('email')
            return func(*args, **kwargs, email=email)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None

        try:
            user = jwt.decode(token, SECRET, algorithms=[TOKEN_ALGO])
            role = user.get('role', 'user')
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != 'admin':
            abort(403)

        return func(*args, **kwargs)

    return wrapper
