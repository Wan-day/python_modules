#!/usr/bin/env python3
import sys


class Arguments():
    def __init__(self) -> None:
        self.len: int = len(sys.argv)
        self.args: list[str] = sys.argv

    def get_len(self) -> int:
        return self.len

    def get_args(self) -> list[str]:
        return self.args

    def print_args(self) -> None:
        print(
                f"Program name: {self.get_args()[0]}\n"
                f"Arguments Recieved: {self.get_len()}"
                )
        if self.len > 1:
            i: int = 1
            while i < self.len:
                print(
                        "Argument "
                        f"{i}"
                        ": "
                        f"{self.get_args()[i]}"
                        )
                i += 1


def main() -> None:
    print("=== Command Quest ===")
    Arguments().print_args()


if __name__ == "__main__":
    main()
