class Event:
    def __init__(self, event_type, event) -> None:
        self._type = event_type
        self._event = event


ENTER = Event('keyboard', 'enter')
