from models.usermodel import usermodel

def authenticate(username,password):
    u=usermodel.get_by_username(username)
    if u and u.password == password:
        return u

def identity(payload):
    user_id = payload['identity']
    u = usermodel.get_by_id(user_id)
    if u :
        return u