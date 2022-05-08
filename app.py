import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main.main import main_blueprint

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)

    return app 

if __name__ == '__main__':
    load_dotenv (find_dotenv ())
    create_app()