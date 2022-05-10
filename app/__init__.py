from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    
    db.init_app(app)
    login_manager.init_app(app)
    
 # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app