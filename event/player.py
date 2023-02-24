from event.event import Event


def play(events: list[Event]) -> None:
    for event in events:
        event.perform()
