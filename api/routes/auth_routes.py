from flask_restful import Resource
from flask import request, jsonify
from controllers.auth_controller import AuthController

class AuthLogin(Resource):
    def post(self):
        return AuthController.login(request.get_json())

class AuthSignup(Resource):
    def post(self):
        return AuthController.signup(request.get_json())


class AuthResetPassword(Resource):
    def post(self):
        return AuthController.reset_password(request.get_json())    

