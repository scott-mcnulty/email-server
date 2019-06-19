from flask import Blueprint
from flask_restful import Api

from server.api.apis import (
    AuthAPI,
    EmailAPI
)

api = Api()

api.add_resource(AuthAPI, '/auth')
api.add_resource(EmailAPI, '/email')
