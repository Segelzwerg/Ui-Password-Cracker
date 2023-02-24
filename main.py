import logging
import sys

from detect_field import find_field
from event.event import ENTER, WAIT_HALF_SEC
from event.player import play
from typer import write
from worldlist.generate import create
from worldlist.word_list import WordList


def main(regex: str) -> None:
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Select the password field by right clicking on it.')
    password_location = find_field()
    logging.debug(f'Password field location: {password_location}')
    confirm_list = [ENTER, WAIT_HALF_SEC, ENTER]
    word_list = create(regex)
    guessed_list = WordList()
    for word in word_list:
        write(word, password_location)
        guessed_list.add(word)
        play(confirm_list)

    guessed_list.to_file('./guessed.txt')

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args[0])
