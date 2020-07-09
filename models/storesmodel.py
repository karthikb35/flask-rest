from db import db


class storesmodel(db.Model):
    __tablename__= 'stores'

    id = db.Column ( db.Integer, primary_key=True )
    name = db.Column ( db.String ( 80 ) )

    items=db.relationship('itemmodel', lazy='dynamic')

    def __init__(self,  name):
        self.name = name


    def jsonify( self ):
        return {'name' : self.name, 'items' : [item.jsonify() for item in self.items.all()]}

    @classmethod
    def get_store ( cls, name ):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self ):
        db.session.add(self)
        db.session.commit()



    def delete_store(self):
        db.session.delete(self)
        db.session.commit()