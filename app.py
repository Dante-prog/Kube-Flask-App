from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
from config import DevelopmentConfig, ProductionConfig
import os
from dotenv import load_dotenv
from my_blueprint import my_blueprint
from models import db

load_dotenv()


def create_app():
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    logging.basicConfig(level=logging.DEBUG)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.register_blueprint(my_blueprint)
    return app, db

app, db = create_app()

class AppFilter(logging.Filter):
    def filter(self, record):
        record.app = "flask-app-dev"
        return True

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(app)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.addFilter(AppFilter())
app.logger.addHandler(handler)

@app.before_request
def log_request_info():
    app.logger.info('Request received from %s for %s with headers %s',
        request.remote_addr, request.path, request.headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)