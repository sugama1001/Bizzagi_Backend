from flask import Flask
from app.routes.register_api import register_routes
from app.tasks.celery_config import make_celery

def create_app():
    app = Flask(__name__)
    celery = make_celery(app)
    register_routes(app)

    return celery, app