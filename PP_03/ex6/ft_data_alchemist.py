#!/usr/bin/env python3

import random

random.seed()

names: list[str] = [
    "Aria", "blaze", "Cipher", "dusk", "Echo",
    "flint", "Gale", "haven", "Ivy", "jinx",
    "Kestrel", "luna", "Maverick", "nova", "Onyx",
    "phoenix", "Quill", "raven", "Sage", "talon",
    "Umber", "vesper", "Willow", "xander", "Yara",
    "zephyr", "Atlas", "briar", "Cobalt", "drake",
]


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    lcase: list[str] = [n for n in names if n[0].islower()]
    ccase: list[str] = [n for n in names if n[0].isupper()]
    l_pts: dict[str, int] = {n: random.randint(0, 1000) for n in lcase}
    l_avg: float = sum(l_pts.values()) / len(l_pts.values())
    l_avg = round(l_avg, 2)
    c_pts: dict[str, int] = {n: random.randint(int(l_avg), 1000) for n in ccase}
    c_avg: float = sum(c_pts.values()) / len(c_pts.values())
    c_avg = round(c_avg, 2)
    print(
            f"Inital list of players: {names}\n"
            f"New list with capitalized players: {ccase}\n"
            f"New list with lowercase players: {lcase}\n"
            f"Score dict for lowercase players: {l_pts}\n"
            f"Average score for lowercase players: {l_avg}\n"
            f"Score dict for capilaized players: {c_pts}\n"
            f"Average score for capitalized players: {c_avg}\n"
            )


if __name__ == "__main__":
    main()
