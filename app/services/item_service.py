from datetime import datetime
from threading import RLock
from uuid import uuid4

from app.exceptions import ItemNotFoundError


class ItemService(object):
    def __init__(self):
        self._items = {}
        self._order = []
        self._lock = RLock()

    def reset(self):
        with self._lock:
            self._items.clear()
            del self._order[:]

    def list(self, offset=0, limit=100):
        with self._lock:
            keys = self._order[offset:offset + limit]
            return [self._items[key] for key in keys]

    def get(self, item_id):
        with self._lock:
            try:
                return self._items[item_id]
            except KeyError:
                raise ItemNotFoundError("Item %s was not found" % item_id)

    def create(self, payload):
        now = datetime.utcnow().isoformat() + "Z"
        item_id = str(uuid4())
        item = dict(payload)
        item.update({"id": item_id, "created_at": now, "updated_at": now})
        with self._lock:
            self._items[item_id] = item
            self._order.append(item_id)
        return item

    def update(self, item_id, payload):
        current = dict(self.get(item_id))
        current.update(payload)
        current["updated_at"] = datetime.utcnow().isoformat() + "Z"
        with self._lock:
            self._items[item_id] = current
        return current

    def delete(self, item_id):
        self.get(item_id)
        with self._lock:
            del self._items[item_id]
            self._order.remove(item_id)


item_service = ItemService()
