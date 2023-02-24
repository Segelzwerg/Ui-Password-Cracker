import logging
import sys

import keyboard

from detect_field import find_field
from event.event import ENTER, WAIT_HALF_SEC
from event.player import play
from typer import write
from worldlist.generate import create

stop_flag = False


def stop() -> None:
    main.stop_flag = True


def main(regex: str) -> None:
    logging.basicConfig(level=logging.DEBUG)
    keyboard.add_hotkey('esc', callback=stop())
    logging.info('Select the password field by right clicking on it.')
    password_location = find_field()
    logging.debug(f'Password field location: {password_location}')
    confirm_list = [ENTER, WAIT_HALF_SEC, ENTER]
    word_list = create(regex)
    for word in word_list:
        if stop_flag:
            break
        write(word, password_location)
        play(confirm_list)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args[0])
