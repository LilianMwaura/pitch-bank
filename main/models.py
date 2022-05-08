from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from ..app import db


class Users(db.model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String , unique = True)

    def __init__(self,name) -> None:
       self.name = name
    
    def __str__(self) -> str:
        return self.name



