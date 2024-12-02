from flask import Flask
import os
from flask_cors import CORS
from db import init_app # Import the database utility
from routes.lottery_numbers import lottery_numbers_bp
from werkzeug.middleware.proxy_fix import ProxyFix

ROOT_DIR = os.path.abspath(os.curdir)

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['DATABASE'] = os.path.join(ROOT_DIR, 'lottery.sqlite')

    # Add ProxyFix middleware with Nginx as single proxy
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,      # Number of proxies setting X-Forwarded-For
        x_proto=1,    # Number of proxies setting X-Forwarded-Proto
        x_host=1,     # Number of proxies setting X-Forwarded-Host
        x_prefix=1    # Number of proxies setting X-Forwarded-Prefix
    )

    # Initialize database-related functionality
    init_app(app)

    # Other configurations or blueprints here
    CORS(app)  # Enable CORS
    app.register_blueprint(lottery_numbers_bp)

    # Routes
    @app.route('/routes')
    def list_routes():
        return '\n'.join([str(rule) for rule in app.url_map.iter_rules()])

    @app.route('/')
    def testing():
        message = {"message": "Hello World"}
        return message

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
