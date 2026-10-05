#!/usr/bin/env python3

class TempError(Exception):
    """Raised when a temperature is outside the range plants can survive."""

    MIN_TEMP = 0
    MAX_TEMP = 40

    def __init__(self, value: int):
        self.value = value
        if (value < self.MIN_TEMP):
            message: str = (
                f"Caught input_temperature error: {value}°C "
                f"is too cold for plants (min {self.MIN_TEMP}°C)"
            )
        else:
            message: str = (
                f"Caught input_temperature error: {value}°C "
                f"is too hot for plants (max {self.MAX_TEMP}°C)"
            )
        super().__init__(message)


def input_temperature(temp_str: str) -> int:
    value = int(temp_str)
    if not TempError.MIN_TEMP <= value <= TempError.MAX_TEMP:
        raise TempError(value)
    return value


def test_temperature() -> None:
    tests: list[str] = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"Input data is: '{test}'")
        try:
            temperature = input_temperature(test)
        except ValueError:
            print(
                "Caught input_temperature error: "
                f"'{test}' is not a valid number\n"
            )
        except TempError as error:
            print(f"{error}\n")
        else:
            print(f"Temperature is now {temperature}°C\n")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
