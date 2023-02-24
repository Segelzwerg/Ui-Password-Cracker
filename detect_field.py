from typing import Tuple

import mouse


def find_field(button: str = mouse.RIGHT) -> Tuple[int, int]:
    mouse.wait(button)
    return mouse.get_position()


if __name__ == '__main__':
    find_field()
