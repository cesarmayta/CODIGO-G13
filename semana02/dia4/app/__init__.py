from flask import Flask

#importamos blueprints
from .admin import admin

def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin)
    
    return app