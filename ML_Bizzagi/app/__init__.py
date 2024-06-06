from flask import Flask
from app.routes.register_api import register_routes
from app.tasks.celery_config import make_celery
from app.tasks.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    celery = make_celery(app)
    register_routes(app)

    return celery, app