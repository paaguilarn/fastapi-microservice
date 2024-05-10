from typing import Any, Callable


subscribers = dict()


def subscribe(event: str, fn: Callable):
    if event not in subscribers:
        subscribers[event] = []
    subscribers[event].append(fn)


def post_event(event: str, data: Any):
    if event not in subscribers:
        pass
    for fn in subscribers[event]:
        fn(data)
