from flask import  request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.itemmodel import itemmodel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument ( 'name',
                          type=str,
                          required=True,
                          help='This field is mandatory'
                          )
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field is mandatory'
    )
    parser.add_argument ( 'store_id',
                          type=int,
                          required=True,
                          help='This field is mandatory'
                          )

    @jwt_required()
    def get( self, name ):
        try:
            item= itemmodel.get_item(name)
            if item:
                return item.jsonify(), 200
            else:
                return {'message' : 'No Item found'},200
        except :
            return {'message' : 'Some error'}, 500

    @jwt_required ( )
    def post( self, name ):
        data= Item.parser.parse_args()
        if itemmodel.get_item(name):
            return {'message': 'Item already present'}, 400
        # item=itemmodel(name, data['price'],data['store_id'])
        item = itemmodel ( **data )
        item.save_to_db()
        return item.jsonify()

    @jwt_required ()
    def delete( self, name ):
        item=itemmodel.get_item(name)
        if item:
            item.delete_item()
            return {'message': 'Element deleted'}, 200
        else:
            return {'messsage' : 'Element not found'}, 400

    @jwt_required()
    def put( self, name ):
        data= Item.parser.parse_args()

        item=itemmodel.get_item(name)
        if item:
            item.price = data['price']
            item.save_to_db ( )
            return item.jsonify ( )
        item=itemmodel(**data)
        item.save_to_db()
        return item.jsonify()

class Itemlist(Resource):
    @jwt_required ( )
    def get( self ):
        return {'items' : [item.jsonify() for item in itemmodel.query.all()]}
