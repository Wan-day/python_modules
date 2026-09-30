#!/usr/bin/env python3

import sys

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def is_number(string: str) -> bool:
    i: int = 0
    j: int = 0
    while i < len(string):
        j = 0
        for n in DIGITS:
            if string[i] == n:
                j = 1
                break
        if j == 0:
            return False
        i += 1
    return True


def to_int(string: str) -> int:
    i: int = 0
    j: int = 0
    num: int = 0
    while i < len(string):
        j = 0
        num = num * 10
        for n in DIGITS:
            if n == string[i]:
                num += j
            else:
                j += 1
        i += 1
    return num


class InvalidInput(Exception):
    def __init__(self, arg: str) -> None:
        self.message = f"Invalid parameter: '{arg}'"
        super().__init__(self.message)


class Arguments():
    def __init__(self) -> None:
        self.len: int = len(sys.argv)
        self.args: list[str] = sys.argv
        self.data = self._parse_args()

    def get_len(self) -> int:
        return self.len

    def get_args(self) -> list[str]:
        return self.args

    def get_data(self) -> list[int]:
        return self.data

    def _parse_args(self) -> list[int]:
        i: int = 1
        data: list[int] = []
        while i < self.len:
            try:
                if is_number(self.args[i]):
                    data = data + [to_int(self.args[i])]
                else:
                    raise InvalidInput(self.args[i])
            except InvalidInput as e:
                print(e)
            finally:
                i += 1
        return data

    def print_data(self) -> None:
        if not self.data:
            print("No scores provided")
        else:
            print(
                    f"Scores processed: {self.data}\n"
                    f"Total players: {len(self.data)}\n"
                    f"Average score : {sum(self.data) / len(self.data)}\n"
                    f"High score: {max(self.data)}\n"
                    f"Low score: {min(self.data)}\n"
                    f"Score range: {max(self.data) - min(self.data)}\n"
                    )


def main() -> None:
    print("=== Player Score Analytics ===\n")
    Arguments().print_data()


if __name__ == "__main__":
    main()
