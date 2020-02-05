from flask_restful import reqparse


class RequestParser():
    def get_body_args(self):
        body_args = reqparse.RequestParser()
        body_args.add_argument('name')
        body_args.add_argument('stars')
        body_args.add_argument('daily_rate')
        body_args.add_argument('city')
        return body_args.parse_args()
