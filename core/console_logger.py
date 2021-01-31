from typing import Any
from core.interface.logger import LoggerInterface


class ConsoleLogger(LoggerInterface):
    def __init__(self) -> None:
        super().__init__()
    
    def debug(self, msg: str, *args: Any):
        print("[DEBUG]", msg, self.__extract_args(args))
    
    def info(self, msg: str, *args: Any):
        print("[INFO]", msg, self.__extract_args(args))
    
    def warning(self, msg: str, *args: Any):
        print("[WARNING]", msg, self.__extract_args(args))
    
    def error(self, msg: str, *args: Any):
        print("[ERROR]", msg, self.__extract_args(args))

    
    def __extract_args(self, *args: Any):
        if args is None:
            return ''
        if len(args) > 0:
            return args