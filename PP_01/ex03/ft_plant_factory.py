#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, h: float, days: int, rate: float) -> None:
        self.name = name
        self.height = h
        self.p_age = days
        self.rate = rate

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.p_age} days old"

    def grow(self) -> None:
        self.height += self.rate
        self.p_age += 1

    def age(self, total: int) -> None:
        for i in range(total):
            self.grow()
            print(f"=== Day {i + 1} ===")
            self.show()
        print(f"Growth this week: {round((total * self.rate), 1)}cm")


def main() -> None:
    print("=== Plant Factory Output ===")

    plants_data = [
        ("Rose", 25, 30, 0.5),
        ("Oak", 200, 365, 2),
        ("Cactus", 5, 90, 0.1),
        ("Sunflower", 80, 45, 0.8),
        ("Fern", 15, 120, 0.25),
    ]

    for plant in plants_data:
        temp = Plant(*plant)
        print(f"Created: {temp.show()}")


if __name__ == "__main__":
    main()
