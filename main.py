import logging
import sys

import keyboard

from event.event import ENTER, WAIT_HALF_SEC
from event.player import play
from ui.detect_field import find_field
from ui.typer import write
from wordlist.generate import create
from wordlist.word_list import WordList

stop_flag = False


def stop() -> None:
    global stop_flag
    stop_flag = True
    logging.debug('Stop requested')


def main(regex: str) -> None:
    logging.basicConfig(level=logging.DEBUG)
    keyboard.add_hotkey('esc', callback=stop)
    logging.info('Select the password field by right clicking on it.')
    password_location = find_field()
    logging.debug(f'Password field location: {password_location}')
    confirm_list = [ENTER, WAIT_HALF_SEC, ENTER]
    word_list = create(regex)
    guessed_list = WordList.from_file('./guessed.txt')
    word_list = word_list.difference(guessed_list)
    global stop_flag
    for word in word_list:
        if stop_flag:
            break
        write(word, password_location)
        guessed_list.add(word)
        play(confirm_list)

    guessed_list.to_file('./guessed.txt')


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args[0])
