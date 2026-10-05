#!/usr/bin/env python3

import random
from typing import Generator

random.seed()

names: tuple[str, ...] = (
    "Aria",
    "Blaze",
    "Cipher",
    "Dusk",
    "Echo",
    "Flint",
    "Gale",
    "Haven",
    "Ivy",
    "Jinx",
    "Kestrel",
    "Luna",
    "Maverick",
    "Nova",
    "Onyx",
    "Phoenix",
    "Quill",
    "Raven",
    "Sage",
    "Talon",
)

actions: tuple[str, ...] = (
    "jump",
    "run",
    "walk",
    "crouch",
    "climb",
    "swim",
    "attack",
    "defend",
    "dodge",
    "block",
    "shoot",
    "reload",
    "heal",
    "cast spell",
    "pick up item",
    "drop item",
    "open door",
    "talk",
    "trade",
    "rest",
)


def gen_event(n: int) -> Generator[tuple[str, str]]:
    for _ in range(n):
        name: str = names[random.randrange(0, len(names))]
        action: str = actions[random.randrange(0, len(actions))]
        yield (name, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str]]:
    while events:
        yield events.pop(0)


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    event: Generator[tuple[str, str]] = gen_event(1000)
    event_list: list[tuple[str, str]] = list()
    for n in range(10):
        data = next(event)
        print(f"Event {n + 1}: {data[0]} just did action {data[1]}")
        event_list.append(data)
    new_events: Generator[tuple[str, str]] = consume_event(event_list)
    print(f"\nA list of generated events: {event_list}\n")
    for i in new_events:
        print(f"Consumed event {i[1]} made by the player {i[0]}")


if __name__ == "__main__":
    main()
