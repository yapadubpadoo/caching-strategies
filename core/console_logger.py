from typing import Any
from core.interface.logger import LoggerInterface


class ConsoleLogger(LoggerInterface):
    def __init__(self) -> None:
        super().__init__()
    
    def debug(self, msg: str, args: Any):
        print("[DEBUG]", msg, args)
    
    def info(self, msg: str, args: Any):
        print("[INFO]", msg, args)
    
    def warning(self, msg: str, args: Any):
        print("[WARNING]", msg, args)
    
    def error(self, msg: str, args: Any):
        print("[ERROR]", msg, args)