import sys

import exrex

from worldlist.word_list import WordList


def create(regex: str) -> WordList:
    return WordList(set(exrex.generate(regex)))


if __name__ == '__main__':
    args = sys.argv[1:]
    print(create(args[0]))
