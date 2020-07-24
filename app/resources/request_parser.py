from flask_restful import reqparse


class RequestParser():
    def get_body_args(self):
        body_args = reqparse.RequestParser()
        body_args.add_argument('name', type=str, required=True,
                               help="The field 'name' is required - (string).")
        body_args.add_argument('stars', type=float, required=True,
                               help="The field 'stars' is required - (float).")
        body_args.add_argument('daily_rate', type=float, required=True,
                               help="The field 'daily rate' is required - (float).")
        body_args.add_argument('city', type=str, required=True,
                               help="The field 'city' is required - (string).")
        return body_args.parse_args()

    def get_body_users_args(self):
        body_args = reqparse.RequestParser()
        body_args.add_argument('name', type=str, required=True,
                               help="The field 'name' is required - (string).")
        body_args.add_argument('login', type=str, required=True,
                               help="The field 'login' is required - (string).")
        body_args.add_argument('password', type=str, required=True,
                               help="The field 'password' is required - (string).")
        return body_args.parse_args()

    def get_params_args(self):
        params_args = reqparse.RequestParser()
        params_args.add_argument('stars_min', type=float, default=0)
        params_args.add_argument('stars_max', type=float, default=5)
        params_args.add_argument('limit', type=float, default=50)
        params_args.add_argument('offset', type=float, default=0)
        params_args.add_argument('city', type=str)
        return params_args.parse_args()
