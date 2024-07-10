from flask import Flask 
from ..config import Config
from .route import init_routes 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 

    init_routes(app) 

    return app 
