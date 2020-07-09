from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from flask_jwt import JWT
from resources.User import UserRegister
from resources.Items import Item, Itemlist
from resources.Stores import StoreList, Store

app=Flask(__name__)
app.secret_key = 'karthik'
api: Api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)