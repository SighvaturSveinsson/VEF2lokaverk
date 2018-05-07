from app import db
from flask_login import UserMixin
from app import login
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    #password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

'''
class Myndir(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(140))
    gallery_nr = db.Column(db.Integer(3))

    def __repr__(self):
        return '<Myndir {}>'.format(self.body)
'''