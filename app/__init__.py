from flask import Flask, jsonify

from app.api.routes.health import health_blueprint
from app.api.routes.items import items_blueprint
from app.config import Config
from app.exceptions import ItemNotFoundError, ValidationError
from app.services.item_service import item_service


def create_app(config=None):
    application = Flask(__name__)
    application.config.from_object(config or Config)
    item_service.reset()

    @application.errorhandler(ItemNotFoundError)
    def handle_not_found(error):
        return jsonify(error="not_found", message=str(error)), 404

    @application.errorhandler(ValidationError)
    def handle_validation(error):
        return jsonify(error="validation_error", details=error.errors), 400

    application.register_blueprint(health_blueprint)
    application.register_blueprint(items_blueprint, url_prefix="/api/v1/items")
    return application
