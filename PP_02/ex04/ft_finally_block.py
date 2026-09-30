#!/usr/bin/env python3

class GardenError(Exception):
    """Raised when there is an error inside the garden"""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    """Raised when there is an error with the plant"""

    def __init__(self, plant_name: str) -> None:
        self.message = f"Invalid plant name to water: '{plant_name}'"
        super().__init__(self.message)


class WaterError(GardenError):
    """Raised when there is an error with the plant"""

    def __init__(self) -> None:
        self.message = "Not enough water in the tank"
        super().__init__(self.message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(plant_name)
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system(test: int) -> None:
    if test == 0:
        tests: list[str] = ["Tomato", "Lettuce", "Carrots"]
    else:
        tests: list[str] = ["Tomato", "lettuce", "carrot"]
    print("Opening water system")
    try:
        for i in tests:
            water_plant(i)
    except PlantError as e:
        print(f"Caught Plant Error: {e}")
    finally:
        print("Finishing up tests and returning to main")
        print("Closing the watering system")


def main() -> None:
    print("=== Garden Watering System ===\n")

    test_watering_system(0)
    test_watering_system(1)


if __name__ == "__main__":
    main()
