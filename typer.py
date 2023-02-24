import logging
from time import sleep
from typing import Tuple

import keyboard
import mouse


def write(word: str, position: Tuple[int, int]) -> None:
    keyboard._os_keyboard.init()  # https://github.com/boppreh/keyboard/issues/446#issuecomment-922032100
    sleep(0.1)
    mouse.move(position[0], position[1])
    mouse.click(button=mouse.LEFT)
    keyboard.press_and_release('tab')  # dirty fix
    sleep(0.1)
    try:
        keyboard.write(word)
    except StopIteration:
        logging.error(f'Could not parse: {word}')
    logging.debug(f'{word} written')
