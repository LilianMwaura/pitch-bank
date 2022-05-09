from flask_sqlalchemy import SQLAlchemy
from ..app import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String , unique = True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String) 
    pitches = db.relationship('Pitch', backref='owner')
    comments = db.relationship('Comment', backref='owner')
    def __repr__(self):
       return f"User('{self.username}')"

# class Categories(db.Model):
#     __tablename__ = 'categories'

#     id= db.Column(db.Integer, primary_key = True)
#     # name = db.Column(db.String)
 
class Pitches(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey ("user.id"), nullable=False)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)  
    def __repr__(self):
            return f'Pitch {self.description}'  
    # category = db.relationship(Categories, backref=db.backref("pitches"), lazy = True)


class Comment(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
    def __repr__(self):
            return f'Comment {self.content}'

    # comment = db.Column(db.Text)

class Votes(db.Model):
      id= db.Column(db.Integer, primary_key = True)
      up_votes = db.Column(db.Integer)
      down_votes = db.Column(db.Integer)
      def __repr__(self):
            return f'Votes{self.votes}'







