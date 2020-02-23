from flask_restful import reqparse


class RequestParser():
    def get_body_args(self):
        body_args = reqparse.RequestParser()
        body_args.add_argument('name', type=str, required=True, help="The field 'name' is required - (string).")
        body_args.add_argument('stars', type=float, required=True, help="The field 'stars' is required - (float).")
        body_args.add_argument('daily_rate', type=float, required=True, help="The field 'daily rate' is required - (float).")
        body_args.add_argument('city', type=str, required=True, help="The field 'city' is required - (string).")
        return body_args.parse_args()

    def get_body_users_args(self):
        body_args = reqparse.RequestParser()
        body_args.add_argument('name', type=str, required=True, help="The field 'name' is required - (string).")
        body_args.add_argument('login', type=str, required=True, help="The field 'login' is required - (string).")
        body_args.add_argument('password', type=str, required=True, help="The field 'password' is required - (string).")
        return body_args.parse_args()
