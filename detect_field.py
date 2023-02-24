import mouse


def find_field(button=mouse.RIGHT) -> (int, int):
    mouse.wait(button)
    return mouse.get_position()


if __name__ == '__main__':
    find_field()
