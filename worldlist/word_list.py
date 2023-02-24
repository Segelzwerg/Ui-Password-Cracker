from typing import Optional, Set


class WordList:
    def __init__(self, words: Optional[Set[str]] = None) -> None:
        self._words: Set[str] = words if words is not None else set()

    def __iter__(self):
        return iter(self._words)

    def add(self, word: str) -> None:
        self._words.add(word)
