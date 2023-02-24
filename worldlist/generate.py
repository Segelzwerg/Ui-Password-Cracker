import sys
from typing import List

import exrex


def create(regex: str) -> List[str]:
    return list(exrex.generate(regex))


if __name__ == '__main__':
    args = sys.argv[1:]
    print(create(args[0]))
