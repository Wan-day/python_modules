#!/usr/bin/env python3

class GardenError(Exception):
    """Raised when there is an error inside the garden"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    """Raised when there is an error with the plant"""

    def __init__(self, plant_name: str) -> None:
        self.message = f"The {plant_name} plant is wilting!"
        super().__init__(self.message)


class WaterError(GardenError):
    """Raised when there is an error with the plant"""

    def __init__(self) -> None:
        self.message = "Not enough water in the tank"
        super().__init__(self.message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        raise PlantError("tomato")
    except PlantError as e:
        print(e)

    try:
        raise WaterError()
    except WaterError as e:
        print(e)

    try:
        raise PlantError("tomato")
    except GardenError as e:
        print(e)

    try:
        raise WaterError()
    except GardenError as e:
        print(e)

    try:
        raise GardenError()
    except GardenError as e:
        print(e)


if __name__ == "__main__":
    main()
