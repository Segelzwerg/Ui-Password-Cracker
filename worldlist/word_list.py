from typing import Optional, Set


class WordList:
    def __init__(self, words: Optional[Set[str]] = None) -> None:
        self._words: Set[str] = words if words is not None else set()

    def __iter__(self):
        return iter(self._words)

    def add(self, word: str) -> None:
        self._words.add(word)

    def to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            for word in self._words:
                file.write(f'{word}\n')
