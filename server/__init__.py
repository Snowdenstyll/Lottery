from flask import Flask
from . import db

def create_app():
    app = Flask(__name__)
    # existing code omitted

    db.init_app(app)

    return app