from abc import ABC, abstractmethod
from typing import Union, Any

class CacheInterface(ABC):
    @abstractmethod
    def set_with_ttl(self, key: str, thing_to_cache: Any, ttl: int) -> bool:
        pass
    
    @abstractmethod
    def get(key: str) -> Any:
        pass