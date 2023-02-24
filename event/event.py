import logging
from abc import abstractmethod
from time import sleep

import keyboard


class Event:
    def __init__(self, event) -> None:
        self._event = event

    @abstractmethod
    def perform(self):
        raise NotImplementedError()


class KeyboardEvent(Event):
    def perform(self):
        keyboard.press_and_release(self._event)
        logging.debug(f'{self._event} pressed')


class MouseEvent(Event):
    pass


class TimeEvent(Event):
    def perform(self):
        sleep(self._event)
        logging.debug(f'{self._event}s waited')


ENTER = KeyboardEvent('enter')
WAIT_HALF_SEC = TimeEvent(0.5)
WAIT_SEC = TimeEvent(1)
WAIT_2_SEC = TimeEvent(2)
