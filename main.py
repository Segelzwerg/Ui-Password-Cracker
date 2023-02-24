import logging

from detect_field import find_field


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Select the password field by right clicking on it.')
    password_location = find_field()
    logging.debug(f'Password field location: {password_location}')


if __name__ == '__main__':
    main()