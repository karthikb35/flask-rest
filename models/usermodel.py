from db import db

class usermodel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column ( db.String ( 80 ) )

    def __init__(self, username,password):

        self.username = username
        self.password = password

    def jsonify( self ):
        return {'username' : self.username, 'password': self.password}

    @classmethod
    def get_by_username( cls, username ):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_id ( cls, id ):
        return cls.query.filter_by ( id=id ).first ( )

    def insert_user( self ):
        db.session.add(self)
        db.session.commit()
