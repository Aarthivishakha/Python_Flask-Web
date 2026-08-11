from uuid import UUID

from flask import Blueprint, jsonify, request

from app.schemas.item import validate_create, validate_update
from app.services.item_service import item_service

items_blueprint = Blueprint("items", __name__)


@items_blueprint.get("")
def list_items():
    try:
        offset = max(int(request.args.get("offset", 0)), 0)
        limit = min(max(int(request.args.get("limit", 100)), 1), 100)
    except ValueError:
        offset, limit = 0, 100
    return jsonify(items=item_service.list(offset, limit))


@items_blueprint.post("")
def create_item():
    payload = validate_create(request.get_json(silent=True) or {})
    return jsonify(item_service.create(payload)), 201


@items_blueprint.get("/<uuid:item_id>")
def get_item(item_id: UUID):
    return jsonify(item_service.get(item_id))


@items_blueprint.patch("/<uuid:item_id>")
def update_item(item_id: UUID):
    payload = validate_update(request.get_json(silent=True) or {})
    return jsonify(item_service.update(item_id, payload))


@items_blueprint.delete("/<uuid:item_id>")
def delete_item(item_id: UUID):
    item_service.delete(item_id)
    return "", 204
