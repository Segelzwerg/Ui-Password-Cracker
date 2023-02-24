from typing import Optional, List


class WordList:
    def __init__(self, words: Optional[List[str]] = None) -> None:
        self._words = words if words is not None else []

    def __iter__(self):
        return iter(self._words)
