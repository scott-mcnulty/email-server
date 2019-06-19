from flask import Flask, jsonify, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity
)

class AuthAPI(Resource):

    def __init__(self):

        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='No `username` supplied.', location='json')
        parser.add_argument('password', type=str, required=True, help='No `password` supplied.', location='json')
        self.parser = parser

    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return {'message': 'Hello, {}'.format(current_user)}

    def post(self):

        args = self.parser.parse_args()
        if args['username'] != 'Us3rnam3' or args['password'] != 'P@ssw0rd':
            return {'message': 'Bad username or password'}, 401

        access_token = create_access_token(identity=args['username'])
        return {'access_token': access_token}, 200
