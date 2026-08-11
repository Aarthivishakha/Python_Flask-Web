from app.exceptions import ValidationError

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)

ALLOWED_FIELDS = set(["name", "description", "price", "active"])


def validate_create(payload):
    errors = _validate(payload, False)
    if errors:
        raise ValidationError(errors)
    return {
        "name": payload["name"].strip(),
        "description": payload.get("description"),
        "price": float(payload["price"]),
        "active": payload.get("active", True),
    }


def validate_update(payload):
    errors = _validate(payload, True)
    if errors:
        raise ValidationError(errors)
    result = dict(payload)
    if "name" in result:
        result["name"] = result["name"].strip()
    if "price" in result:
        result["price"] = float(result["price"])
    return result


def _validate(payload, partial):
    errors = []
    unknown = set(payload.keys()) - ALLOWED_FIELDS
    if unknown:
        errors.append("Unknown fields: " + ", ".join(sorted(unknown)))
    if not partial and "name" not in payload:
        errors.append("name is required")
    if not partial and "price" not in payload:
        errors.append("price is required")
    if "name" in payload and not isinstance(payload["name"], string_types):
        errors.append("name must be a string")
    elif "name" in payload and not payload["name"].strip():
        errors.append("name must not be empty")
    if "price" in payload:
        try:
            if float(payload["price"]) < 0:
                errors.append("price must be non-negative")
        except (TypeError, ValueError):
            errors.append("price must be a number")
    if "active" in payload and not isinstance(payload["active"], bool):
        errors.append("active must be a boolean")
    return errors
