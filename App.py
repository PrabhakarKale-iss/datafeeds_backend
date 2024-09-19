from flask import Flask, jsonify
from Common.db import init_db
from routes.client_company import client_company_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(client_company_bp, url_prefix='/companies')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
