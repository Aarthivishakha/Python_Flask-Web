from datetime import datetime, timezone
from threading import RLock
from uuid import UUID, uuid4

from app.exceptions import ItemNotFoundError


class ItemService:
    def __init__(self) -> None:
        self._items: dict[UUID, dict] = {}
        self._order: list[UUID] = []
        self._lock = RLock()

    def reset(self) -> None:
        with self._lock:
            self._items.clear()
            del self._order[:]

    def list(self, offset: int = 0, limit: int = 100) -> list[dict]:
        with self._lock:
            keys = self._order[offset:offset + limit]
            return [self._items[key] for key in keys]

    def get(self, item_id: UUID) -> dict:
        with self._lock:
            try:
                return self._items[item_id]
            except KeyError:
                raise ItemNotFoundError(f"Item {item_id} was not found")

    def create(self, payload: dict) -> dict:
        now = datetime.now(timezone.utc).isoformat()
        item_id = uuid4()
        item = {"id": str(item_id), "created_at": now, "updated_at": now, **payload}
        with self._lock:
            self._items[item_id] = item
            self._order.append(item_id)
        return item

    def update(self, item_id: UUID, payload: dict) -> dict:
        current = self.get(item_id)
        updated = {**current, **payload, "updated_at": datetime.now(timezone.utc).isoformat()}
        with self._lock:
            self._items[item_id] = updated
        return updated

    def delete(self, item_id: UUID) -> None:
        self.get(item_id)
        with self._lock:
            del self._items[item_id]
            self._order.remove(item_id)


item_service = ItemService()
