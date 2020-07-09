from flask_restful import Resource,reqparse
from models.usermodel import usermodel

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
    parser.add_argument ( 'password',
                          type=str,
                          required=True,
                          help='This field cannot be blank' )
    def post( self ):
        request_receivd=UserRegister.parser.parse_args()

        if usermodel.get_by_username(request_receivd['username']):
            return {'message' : 'user already exists'}, 400
        # user = usermodel.insert_user(request_receivd['username'],request_receivd['password'])
        user = usermodel( **request_receivd)
        user.insert_user()
        return user.jsonify()
