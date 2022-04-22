from flask import Flask

#importamos blueprints
from .admin import admin
from .portafolio import portafolio

#importamos config
from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(admin)
    app.register_blueprint(portafolio)
    
    return app