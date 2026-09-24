#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float,
            ) -> None:
        self.name = name
        self.rate = rate
        self._stats = self._Stats()
        if (height < 0):
            self._height = 10.0
        else:
            self._height = height
        if (days < 0):
            self._p_age = 15
        else:
            self._p_age = days

    def show(self) -> None:
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._p_age} days old"
        )
        self._stats._show_inc()

    def grow(self) -> None:
        self._height += self.rate
        self._stats._grow_inc()

    def age(self, total: int) -> None:
        print(f"[the plant is aging {total} days]")
        for i in range(total):
            self._height += self.rate
            self._p_age += 1
        print(f"Growth after {total} days: {round(total * self.rate, 1)}cm")
        self._stats._age_inc()

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

    @staticmethod
    def is_year_old(days_old: int) -> bool:
        if (days_old > 364):
            return True
        else:
            return False

    @classmethod
    def anon(cls) -> "Plant":
        return cls("None", 0, 0, 0)

    class _Stats():
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def _grow_inc(self) -> None:
            self._grow_count += 1

        def _age_inc(self) -> None:
            self._age_count += 1

        def _show_inc(self) -> None:
            self._show_count += 1

        def get_data(self) -> dict:
            return ({
                "grow_count": self._grow_count,
                "age_count": self._age_count,
                "show_count": self._show_count
                })


class Flower(Plant):
    is_bloom = False

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float,
            color: str
            ) -> None:
        super().__init__(
                name,
                height,
                days,
                rate
                )
        self.color = color

    def bloom(self) -> None:
        self.is_bloom = True
        print(f"[asking the {self.name} to bloom]")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.is_bloom):
            print(f" {self.name} is blooming beatifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    seeds = 0

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float,
            color: str
            ) -> None:
        super().__init__(
                name,
                height,
                days,
                rate,
                color
                )

    def bloom(self) -> None:
        self.is_bloom = True
        print(f"[asking the {self.name} to bloom]")
        self.seeds += 21

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float,
            trunk_size: float
            ) -> None:
        super().__init__(
                name,
                height,
                days,
                rate
                )
        self.t_size = trunk_size

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.t_size, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.t_size}cm wide."
            )
        self._Stats()._shade_inc()

    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def _shade_inc(self) -> None:
            self._shade_count += 1

        def get_data(self) -> dict:
            return ({
                "grow_count": self._grow_count,
                "age_count": self._age_count,
                "show_count": self._show_count,
                "shade_count": self._shade_count
                })


class Vegetable(Plant):
    n_value = 0

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float,
            harvest_season: str,
            ) -> None:
        super().__init__(
                name,
                height,
                days,
                rate
                )
        self.h_season = harvest_season

    def show(self) -> None:
        super().show()
        print(
            f" Harvest season: {self.h_season}\n"
            f" Nutritional value: {self.n_value}"
            )

    def age(self, total: int) -> None:
        for i in range(total):
            self.n_value += 1
            self._height += self.rate
            self._p_age += 1
        print(f"[make {self.name} grow and age for {total} days]")


def print_stats(plant: Plant) -> None:
    stats = plant._stats.get_data()
    if ("shade_count" in stats):
        print(
            f"Stats: {stats["grow_count"]} grow, "
            f"{stats["age_count"]} age, "
            f"{stats["show_count"]} show, "
            f"{stats["shade_count"]} shade"
            )
    else:
        print(
            f"Stats: {stats["grow_count"]} grow, "
            f"{stats["age_count"]} age, "
            f"{stats["show_count"]} show"
            )


def main() -> None:
    print("=== Garden Statistics ===")
    print("=== Flower")

    rose = Flower("Rose", 15, 10, 0.5, "red")
    rose.show()
    rose.age(10)
    rose.grow()
    print_stats(rose)

    print("\n=== Tree")

    oak = Tree("Oak", 200, 365, 2, 10)
    oak.show()
    oak.produce_shade()
    oak.age(5)
    print_stats(oak)

    print("\n=== Vegetable")

    tomato = Vegetable("Tomato", 5, 10, 0.5, "April")
    tomato.show()
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
