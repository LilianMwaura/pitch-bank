from flask import Flask
from .main.main import main_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    return app 

if __name__ == '__main__':
    create_app()