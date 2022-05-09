import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .main.main import main_blueprint

# from .main import models

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
from .main import models
def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_blueprint)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)
    migrate = Migrate(app,db)
    login_manager.init_app(app)


    return app 

if __name__ == '__main__':
    load_dotenv (find_dotenv ())
    create_app()