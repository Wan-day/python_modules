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
    print("=== Cyber Archives Recovery & Preservation ===")
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
        lines: list[str] = data.splitlines()
        lines = [line + "#" for line in lines]
        output: str = "\n".join(lines)
        print(
                "\nUpdating the file\n"
                "New updated version:\n"
                )
        print(output)
        sys.stdout.write("Please write a new file name: ")
        sys.stdout.flush()
        new_fn: str = sys.stdin.readline().rstrip("\n")
        if new_fn == "":
            print("No new finelane provided, discarding the changes")
        else:
            output_file: IO[str] = open(new_fn, "w")
            print(f"Creating file: {new_fn}")
            try:
                print(f"Writing into a file: {new_fn}")
                output_file.write(output)
            finally:
                print(f"Closing file: {new_fn}")
                output_file.close()
    except (NoArgument, FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error: {e}\n")


if __name__ == "__main__":
    main()
