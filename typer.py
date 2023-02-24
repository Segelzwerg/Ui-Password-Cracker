from time import sleep

import keyboard


def write(word: str) -> None:
    keyboard._os_keyboard.init()  # https://github.com/boppreh/keyboard/issues/446#issuecomment-922032100
    sleep(0.1)
    keyboard.write(word)


if __name__ == '__main__':
    write('test')
