from flask import Flask
import os
from flask_cors import CORS
# Import the database utility
from server.db import init_app
from server.routes.user import user_bp  # Import the user blueprint

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['DATABASE'] = os.path.join(app.instance_path, 'lottery.sqlite')

    # Initialize database-related functionality
    init_app(app)

    # Other configurations or blueprints here
    CORS(app)  # Enable CORS
    app.register_blueprint(user_bp)

    # Routes
    @app.route('/routes')
    def list_routes():
        return '\n'.join([str(rule) for rule in app.url_map.iter_rules()])

    @app.get("/wtf")
    def testing():
        message = {"message": "Hello World"}
        return message

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()