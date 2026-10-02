#!/usr/bin/env python3

import math


class InvalidInput(Exception):
    def __init__(self, arg: str) -> None:
        self.message = f"Invalid parameter: '{arg}'"
        super().__init__(self.message)


class Coordinates():
    def _get_player_1_pos(self) -> None:
        result: list[float] = []
        coords: list[str] = input(
                "Enter new coordinates"
                " as floats in format"
                " 'x,y,z': "
                ).split(",", 2)
        try:
            for data in coords:
                result.append(float(data))
            self.p_1_pos: tuple[float, ...] = tuple(result)
            print(
                    f"Got a first tuple: {self.p_1_pos}\n"
                    f"It includes: X={self.p_1_pos[0]}, "
                    f"Y={self.p_1_pos[1]} "
                    f"Z={self.p_1_pos[2]}"
                    )
        except ValueError as e:
            print(
                    "Error on parameter: "
                    f"'{coords[len(coords) - len(result) - 1]}': "
                    f"{e}"
                  )
            raise InvalidInput(coords[len(coords) - len(result) - 1])

    def _get_player_2_pos(self) -> None:
        result: list[float] = []
        coords: list[str] = input(
                "Enter new coordinates"
                " as floats in format"
                " 'x,y,z': "
                ).split(",", 2)
        try:
            for data in coords:
                result.append(float(data))
            self.p_2_pos: tuple[float, ...] = tuple(result)
            print(
                    f"Got a second tuple: {self.p_2_pos}\n"
                    f"It includes: X={self.p_2_pos[0]}, "
                    f"Y={self.p_2_pos[1]} "
                    f"Z={self.p_2_pos[2]}"
                    )
        except ValueError as e:
            print(
                    "Error on parameter: "
                    f"'{coords[len(coords) - len(result) - 1]}': "
                    f"{e}"
                  )
            raise InvalidInput(coords[len(coords) - len(result) - 1])

    def calculate_distance(self) -> None:
        try:
            self._get_player_1_pos()
            x1 = self.p_1_pos[0]
            y1 = self.p_1_pos[1]
            z1 = self.p_1_pos[2]
            p_1_center: float = math.sqrt((x1-0)**2 + (y1-0)**2 + (z1-0)**2)
            print(f"Distance to center: {round(p_1_center, 3)}\n")
            self._get_player_2_pos()
            x2 = self.p_2_pos[0]
            y2 = self.p_2_pos[1]
            z2 = self.p_2_pos[2]
            p_2_center: float = math.sqrt((x2-0)**2 + (y2-0)**2 + (z2-0)**2)
            print(f"Distance to center: {round(p_2_center, 3)}\n")
            p_distance: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(
                    "Distance between the 2 sets of coordinates: "
                    f"{round(p_distance, 3)}"
                    )
        except InvalidInput:
            pass


def main() -> None:
    print("=== Game Coordinate System ===\n")
    args = Coordinates()
    args.calculate_distance()


if __name__ == "__main__":
    main()
