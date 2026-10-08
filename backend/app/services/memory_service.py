from __future__ import annotations

import json
from typing import Any, Dict

try:
    import redis.asyncio as redis
except Exception:  # pragma: no cover
    redis = None


class MemoryService:
    def __init__(self, redis_url: str | None = None):
        self._store: Dict[str, Any] = {}
        self.redis_url = redis_url
        self.redis_client = None
        if redis:
            try:
                self.redis_client = redis.from_url(redis_url or "redis://localhost:6379/0")
            except Exception:  # pragma: no cover
                self.redis_client = None

    async def set(self, key: str, value: Any) -> None:
        if self.redis_client:
            await self.redis_client.set(key, json.dumps(value))
        self._store[key] = value

    async def get(self, key: str, default: Any = None) -> Any:
        if self.redis_client:
            value = await self.redis_client.get(key)
            if value is not None:
                return json.loads(value)
        return self._store.get(key, default)

    async def delete(self, key: str) -> None:
        if self.redis_client:
            await self.redis_client.delete(key)
        self._store.pop(key, None)


memory_service = MemoryService()
