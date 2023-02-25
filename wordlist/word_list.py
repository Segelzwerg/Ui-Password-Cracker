import logging
from typing import Optional, Set, Self


class WordList:
    def __init__(self, words: Optional[Set[str]] = None) -> None:
        self._words: Set[str] = words if words is not None else set()

    def __iter__(self):
        return iter(self._words)

    def __len__(self):
        return len(self._words)

    def __str__(self):
        return str(self._words)

    def add(self, word: str) -> None:
        self._words.add(word)

    def to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            for word in self._words:
                file.write(f'{word}\n')

    def difference(self, other: Self) -> Self:
        new_set = self._words - other._words
        return WordList(new_set)

    @classmethod
    def from_file(cls, path: str) -> Self:
        with open(path, 'r') as file:
            lines = set(file.read().splitlines())
            logging.info(f'Loaded {len(lines)} already guessed passwords')
            return WordList(lines)

        return WordList()
