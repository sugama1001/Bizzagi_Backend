from app.routes.api import blueprint_ml as ml_api

def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(ml_api)