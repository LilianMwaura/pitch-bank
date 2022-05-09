from flask_sqlalchemy import SQLAlchemy
from ..app import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String , unique = True)
    email = db.Column(db.String)
    def __init__(self,name) -> None:
       self.name = name
    
    def __str__(self) -> str:
        return self.name

class Categories(db.Model):
    id= db.Colomn(db.Integer, primary_key = True)
    name = db.Column(db.String)
 
class Pitches(db.Model):
    __tablename__ = 'pitches'
    id= db.Colomn(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey ["categories.id"])
    category = db.relationship(Categories) 
    
class Comment(db.Model):
    id= db.Colomn(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
class Votes(db.Model):
      id= db.Colomn(db.Integer, primary_key = True)
      up_votes = db.Column(db.Integer)
      down_votes = db.Column(db.Integer)






