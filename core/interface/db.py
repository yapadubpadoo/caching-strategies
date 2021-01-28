from abc import ABC, abstractmethod
from typing import Any, Union

class DBInterface(ABC):
    @abstractmethod
    def upsert(self, object: dict) -> int:
        pass

    @abstractmethod
    def find_one_by_id(self, id: Any) -> Union[dict, None]:
        pass
