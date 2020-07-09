from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.storesmodel import storesmodel

class Store(Resource):

    @jwt_required ( )
    def get ( self, name ):
        try:
            store = storesmodel.get_store ( name )
            if store:
                return store.jsonify ( ), 200
            else:
                return {'message': 'No Store found'}, 200
        except:
            return {'message': 'Some error'}, 500

    @jwt_required()
    def post( self,name  ):


        if storesmodel.get_store(name):
            return {'message' : 'Store already exists'}, 400
        # user = usermodel.insert_user(request_receivd['username'],request_receivd['password'])
        store = storesmodel( name)
        store.save_to_db()
        return store.jsonify()

    @jwt_required()
    def delete( self, name ):
        store = storesmodel.get_store ( name )
        if store:
            try:
                store.delete()
                return {'message': 'Store deleted'}, 200
            except:
                return {'message'  : 'Error deleting store'} , 500
        else:
            return {'messsage': 'Store not found'}, 400

class StoreList(Resource):
    @jwt_required ( )
    def get( self ):
        return {'stores' : [store.jsonify() for store in storesmodel.query.all()]}