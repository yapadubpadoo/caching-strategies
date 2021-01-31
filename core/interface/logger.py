from abc import ABC, abstractmethod
from typing import Any, Union

class LoggerInterface:
    @abstractmethod
    def debug(self, message: str, args: Any):
        pass

    def info(self, message: str, args: Any):
        pass

    def warning(self, message: str, args: Any):
        pass

    def error(self, message: str, args: Any):
        pass
