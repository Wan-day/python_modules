#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, h: float, days: int, rate: float) -> None:
        self.name = name
        self.height = h
        self.days = days
        self.rate = rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += self.rate
        self.days += 1

    def age(self, total: int) -> None:
        for i in range(total):
            self.grow()
            print(f"=== Day {i + 1} ===")
            self.show()
        print(f"Growth this week: {round((total * self.rate), 1)}cm")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 25, 0.4)
    rose.show()
    rose.age(7)


if __name__ == "__main__":
    main()
