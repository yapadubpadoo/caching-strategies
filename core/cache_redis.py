from core.interface.cache import CacheInterface
from typing import Any

class RedisCache(CacheInterface):
    def __init__(self, redis_connection) -> None:
        super().__init__()
        self.cache = redis_connection

    def set_with_ttl(self, key: str, thing_to_cache: Any, ttl: int) -> bool:
        return self.cache.set(key, thing_to_cache, ex=ttl)
    
    def get(self, key: str) -> Any:
        return self.cache.get(key)