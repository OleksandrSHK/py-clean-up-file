import os
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Type[Any]) -> None:
        self.file.close()
        os.remove(self.filename)
