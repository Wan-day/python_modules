#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, h: float, days: int, rate: float) -> None:
        self.name = name
        self.rate = rate
        if (h < 0):
            self._height = 10.0
        else:
            self._height = h
        if (days < 0):
            self._p_age = 15
        else:
            self._p_age = days

    def show(self) -> str:
        return (
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._p_age} days old"
        )

    def grow(self) -> None:
        self._height += self.rate
        self._p_age += 1

    def age(self, total: int) -> None:
        for i in range(total):
            self.grow()
            print(f"=== Day {i + 1} ===")
            self.show()
        print(f"Growth this week: {round(total * self.rate, 1)}cm")

    def set_height(self, height: float) -> None:
        if (height < 0):
            self._error("height")
        else:
            self._height = height
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, days: int) -> None:
        if (days < 0):
            self._error("age")
        else:
            self._p_age = days
            print(f"Age updated: {self._p_age} days")

    def _error(self, msg: str) -> None:
        if (msg == "height"):
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )
        elif (msg == "age"):
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )


def main() -> None:
    print("=== Garden Plant Type ===")
    print("=== FLower")

    rose = Plant("Rose", 15, 10, 0.5)

    print("=== Tree")
    print("=== Vegetable")


if __name__ == "__main__":
    main()
