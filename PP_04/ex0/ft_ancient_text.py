#!/usr/bin/env python3

import sys
from typing import IO


class InvalidInput(Exception):
    template: str = "Invalid parameter: '{}'"

    def __init__(self, arg: str) -> None:
        self.message = self.template.format(arg)
        super().__init__(self.message)


class NoArgument(InvalidInput):
    template: str = "No argument provided"

    def __init__(self) -> None:
        self.message = self.template
        super().__init__(self.message)


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    try:
        if len(sys.argv) < 2:
            raise NoArgument()
        filename: str = sys.argv[1]
        file: IO[str] = open(filename, 'r')
        try:
            data: str = file.read()
            print(f"Accessing file: {filename}")
            print(
                    "---\n"
                    f"{data}\n"
                    "---"
                    )
        finally:
            print(f"Closing file: {filename}")
            file.close()
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except NoArgument as e:
        print(e)


if __name__ == "__main__":
    main()
