import logging

from detect_field import find_field
from event.event import ENTER, WAIT_HALF_SEC
from event.player import play
from typer import write


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Select the password field by right clicking on it.')
    password_location = find_field()
    logging.debug(f'Password field location: {password_location}')
    confirm_list = [ENTER, WAIT_HALF_SEC, ENTER]
    write('password', password_location)
    play(confirm_list)


if __name__ == '__main__':
    main()
