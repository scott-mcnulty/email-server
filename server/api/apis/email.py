import json

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from yagmail import SMTP

from server import config
from server.commons.log import log


class EmailAPI(Resource):

    def __init__(self):

        parser = reqparse.RequestParser()
        parser.add_argument('from', type=str, required=True, help='No `from` supplied.', location='json')
        parser.add_argument('subject', type=str, required=True, help='No `subject` supplied.', location='json')
        parser.add_argument('content', type=str, required=True, help='No `content` supplied.', location='json')
        self.parser = parser

        self.yag = SMTP('YOUR_EMAIL_HERE', oauth2_file="./credentials.json")

    # @jwt_required
    def post(self):

        # Gets the supplied args
        args = self.parser.parse_args()
        log('got arguments: {}'.format(args))
        _from = args.get('from')
        subject = args.get('subject')
        content = args.get('content')
        contents = 'From: {}. \n Content: {}'.format(_from, content)

        self.yag.send(
            subject=subject,
            contents=contents
        )

        return {
            'from': _from,
            'subject': subject,
            'content': content
        }
