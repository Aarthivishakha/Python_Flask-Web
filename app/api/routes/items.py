from flask import Blueprint, jsonify, request

from app.schemas.item import validate_create, validate_update
from app.services.item_service import item_service

items_blueprint = Blueprint("items", __name__)


@items_blueprint.route("", methods=["GET"])
def list_items():
    try:
        offset = max(int(request.args.get("offset", 0)), 0)
        limit = min(max(int(request.args.get("limit", 100)), 1), 100)
    except ValueError:
        offset, limit = 0, 100
    return jsonify(items=item_service.list(offset, limit))


@items_blueprint.route("", methods=["POST"])
def create_item():
    payload = validate_create(request.get_json(silent=True) or {})
    return jsonify(item_service.create(payload)), 201


@items_blueprint.route("/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify(item_service.get(item_id))


@items_blueprint.route("/<item_id>", methods=["PATCH"])
def update_item(item_id):
    payload = validate_update(request.get_json(silent=True) or {})
    return jsonify(item_service.update(item_id, payload))


@items_blueprint.route("/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    item_service.delete(item_id)
    return "", 204
